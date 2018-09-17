from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

def search(commodity=None):
    print("Begin Search")
    driver.get('https://www.taobao.com')
    try:
        input = wait.until(
            EC.presence_of_element_located( (By.CSS_SELECTOR,'#q') )
        )
        input.send_keys(u'{}'.format(commodity))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        submit.click()
        get_response()
    except TimeoutError:
        return search(commodity)

def get_response():
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-itemlist  .items .item'))
    )
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    items = soup.find('div', class_='m-itemlist').find_all('div',class_='item')

    for item in items:
        product = {
            'image':item.find('a').find('img')['src'],
            'price':item.find('div',class_='price g_price g_price-highlight').text,
            'buyer_num':item.find('div',class_='deal-cnt').text[:-3],
            'title':item.find('div',class_='row row-2 title').text,
            'location':item.find('div', class_='location').text,
        }
        print(product)

def goto_next_page(page):
    print("current is on page {}".format(page))
    try:
        input=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()
        input.send_keys(page)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager >div >div >div >ul >li.item.active >span'),str(page))
        )
    except TimeoutError:
        return goto_next_page(page)

    get_response()

if __name__ == '__main__':
    commodity = input("Pleae input the name fo commodity:")
    search(commodity)
    for i in range(2,10):
        goto_next_page(i)