# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from anime_scraper.models import insert_genre

class AnimeScraperPipeline:
    def process_item(self, item, spider):
        return item

class GenreScraperPipeline:
    def process_item(self,item,spider):
        id=item['id']
        name=item['name']
        insert_genre(id,name)

