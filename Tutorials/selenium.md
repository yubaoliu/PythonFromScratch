

# Quick Start

**Example**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys("python")
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(20)
driver.quit()

```

**Important**: make sure [ChromeDriver - WebDriver for Chrome](http://chromedriver.chromium.org/) is already putted in the recognized position



"