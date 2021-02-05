import scrapy
import re
from aaai.items import PlenaryItem
import requests
import json

class PlenariesSpider(scrapy.Spider):
    name = 'plenaries'
    allowed_domains = ['virtual.2021.aaai.org','slideslive.com','cloudfront.net']
    start_urls = ['https://virtual.2021.aaai.org/plenary_sessions.html']

    def start_requests(self):
        request = scrapy.Request(self.start_urls[0], cookies=self.settings.get('COOKIES'), callback=self.parse)
        return [request]

    def parse(self, response):
        all_links = response.xpath("//a[@class='main-title']")
        for item in all_links:
            yield response.follow(item.xpath("@href").get(), callback=self.parse_id)

    def parse_id(self, response):
        element = response.xpath("//script[contains(text(),'presentationId')]").get()
        so_pattern = re.compile(r"presentationId:\s'(\d*?)'", re.MULTILINE|re.DOTALL)
        result = re.findall(so_pattern, element)[0]

        res_url = requests.get("https://ben.slideslive.com/player/{}?demo=false".format(result)).json()

        if 'slides_json_url' in res_url:
            res = PlenaryItem()
            res["pic_id"] = result
            all_ids = requests.get(res_url['slides_json_url']).json()['slides']
            res["image_urls"] = []
            for item in all_ids:
                res["image_urls"].append("https://d2ygwrecguqg66.cloudfront.net/data/presentations/{}/slides/medium/{}.jpg".format(result, item["image"]["name"]))
            yield res
