import scrapy
from aaai.items import AaaiItem
class PapersSpider(scrapy.Spider):
    name = 'papers'
    allowed_domains = ['virtual.2021.aaai.org']
    start_urls = ['https://virtual.2021.aaai.org/papers.json']

    def start_requests(self):
        request = scrapy.Request(self.start_urls[0], cookies=self.settings.get('COOKIES'), callback=self.parse
        )
        return [request]

    def parse(self, response):
        res = response.json()
        for item in res:
            content = item['content']
            resItem = AaaiItem()
            resItem['title'] = content['title']
            resItem['abstract'] = content['abstract']
            resItem['names'] = ",".join(content['authors'])
            resItem['track'] = content['program']
            resItem['file_urls'] = [content['pdf_url']]
            yield resItem
