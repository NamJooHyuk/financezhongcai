#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_zhongcDB = client[settings['MONGODB_DB']]
collect_zhongc_161212 = News_zhongcDB[settings['MONGODB_COLLECTION']]