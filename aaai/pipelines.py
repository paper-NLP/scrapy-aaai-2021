# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class AaaiPipeline:
    def process_item(self, item, spider):
        return item

class DownloadPdfPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, item=None):
        print(item['track'] + "/" + item['title'] + ".pdf")
        return item['track'] + "/" + item['title'] + ".pdf"
    