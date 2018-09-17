# -*- coding: utf-8 -*-
import re
import urllib.request

import scrapy
from scrapy_spider.items import ScrapySpiderItem

class XicidailiSpiderSpider(scrapy.Spider):
    name = 'xicidaili_spider'
    allowed_domains = ['xicidaili.com']
    home_page ="http://xicidaili.com"
    start_urls = ['http://xicidaili.com/']

    def start_requests(self):
        reqs = []
        for i in range(1,3000): #Modifi the page number here
            req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
            reqs.append(req)
        return  reqs

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')

        items = []

        # 提取ip和端口
        #ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", res, re.S)

        for ip in trs[1:]:
            pre_item = ScrapySpiderItem()
            pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()
            pre_item['POSITION'] = ip.xpath('string(td[4])')[0].extract().strip()
            pre_item['TYPE']=ip.xpath('td[6]/text()')[0].extract()
            pre_item['SPEED']=ip.xpath('td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
            pre_item['ALIVE']=ip.xpath('td[9]/text()')[0].extract()
            pre_item['LAST_CHECK_TIME']=ip.xpath('td[10]/text()')[0].extract()

            items.append(pre_item)

            #Get longer alive IPs
            # res = re.match(r'(.*?)天', pre_item['ALIVE'])
            # if res:
            #     print(res.group(1))
            #     if self.verify_ip(pre_item['IP'],pre_item['PORT'], pre_item['TYPE']):
            #         items.append(pre_item)

        return items