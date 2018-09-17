# -*- coding: utf-8 -*-
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapySpiderPipeline(object):
    def __init__(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.xicidaili_db = myclient['Proxy']
        self.xicidaili_col = self.xicidaili_db['xicidaili']
        collist = self.xicidaili_db.list_collection_names()
        if "xicidaili" in collist:
            self.xicidaili_col.delete_many({})
            print("------------xicidaili_col is not created------------")

    def process_item(self, item, spider):
        itemDict ={
            'IP': item['IP'],
            'PORT':item['PORT'],
            'POSITION':item['POSITION'],
            'TYPE':item['TYPE'],
            'SPEED': item['SPEED'],
            'ALIVE':item['ALIVE'],
            'LAST_CHECK_TIME':item['LAST_CHECK_TIME']
        }
        myquery = {"IP":item['IP']}
        try:
            if self.xicidaili_col.find(myquery):
                self.xicidaili_col.delete_one(myquery)
            res = self.xicidaili_col.insert_one(itemDict)
        except:
            print("MongoDB failed on: "+ item)

        return item

    def close_spider(self, spider):
        pass
