# -*- coding: utf-8 -*-
import scrapy
from practice.items import PracticeItem


class AkaSpider(scrapy.Spider):
    name = 'aka'
#    allowed_domains = ['https://www.w3schools.com/pHP/default.asp']
    start_urls = ['https://www.w3schools.com/pHP/php_intro.asp']

    def parse(self, response):
		print (response.xpath('//div/text()').extract()[-8])
		print (response.xpath('//div/text()').extract()[-10])
		print ("radhe radhe")
		print ("-----------------------------------------")




        
