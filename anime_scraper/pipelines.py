# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from anime_scraper.models import insert_genre, insert_studio,insert_rank,insert_link

class AnimeScraperPipeline:
    def process_item(self, item, spider):
        return item

class AnimeLinkScraperPipeline:
    def process_item(self,item,spider):
        if item['type']=='url':
            url=item['link']
            txt=url.split('/')
            mal_id=int(txt[txt.index('anime')+1])
            insert_link(url,mal_id)


class GenreScraperPipeline:
    def process_item(self,item,spider):
        id=item['id']
        name=item['name']
        type=item['type']
        if type == 'genre':
            insert_genre(id,name)
        elif type=='studio':
            insert_studio(id,name)
        elif type=='rank':
            insert_rank(name)

