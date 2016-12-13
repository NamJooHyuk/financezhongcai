#encoding:utf-8
import scrapy
import re
from scrapy.selector import Selector
from financezhongc.items import FinancezhongcItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class ExampleSpider(CrawlSpider):
    name = "zhongcnews"
    allowed_domains = ["www.cfi.net.cn"]
    start_urls = ['http://www.cfi.net.cn/']
    rules=(
        Rule(LinkExtractor(allow=r"/\D20161212[a-zA-Z0-9\.]+"),
        callback="parse_news",follow=True),
    )
    def printcn(suni):
        for i in uni:
            print uni.encode('utf-8')
    def parse_news(self,response):
        item = FinancezhongcItem()
        item['news_thread']=response.url.strip().split('/')[-1][:-5]
        # self.get_thread(response,item)
        self.get_title(response,item)
        self.get_time_from(response,item)
        self.get_url(response,item)
        self.get_text(response,item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        return item 
    def get_title(self,response,item):
        title=response.xpath("/html/head/title/text()").extract()
        if title:
            # print 'title:'+title[0][:-5].encode('utf-8')
            item['news_title']=title[0][:-6]

    def get_time_from(self,response,item):
        time_from=response.xpath("//div[@id='tdcontent']/table/tbody/tr/td[2]/text()").extract()
        if time_from:
            # print 'time'+time[0][:-5].encode('utf-8')
            item['news_time']=time_from[0]

    def get_text(self,response,item):
        news_body=response.xpath("//div[@id='tdcontent']/text() | //div[@id='tdcontent']/a/text()").extract()
        if news_body:
            # for  entry in news_body:
            #   print entry.encode('utf-8')
            item['news_body']=news_body 
    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            #print news_url 
            item['news_url']=news_url
