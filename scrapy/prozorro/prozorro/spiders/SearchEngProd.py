# -*- coding: utf-8 -*-
import scrapy


class SearchengprodSpider(scrapy.Spider):
    name = "SearchEngProd"
    allowed_domains = ["https://prozorro.gov.ua/"]
    start_urls = ['http://https://prozorro.gov.ua/tender/search/?cpv=71323000-8/']

    def parse(self, response):
	    tendercnt = response.css('div.result-all span')..extract_first() 
        tenderlist = response.css('div.items-list')
		for tender in tenderlist:
		   tenderitem = ProzorroItem()
		   tenderitem['id'] = tender.css('div.col-md-8 a::attr(href)').extract_first()
		   tenderitem['name'] = tender.css('div.col-md-8 a span').extract_first()
		   yield tenderitem
		   
		yield [FormRequest("https://prozorro.gov.ua/tender/form/search"
		        , 
				, callback=self.parse_ajax)]
		
	def parse_ajax(self,response)
	   pass
