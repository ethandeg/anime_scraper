import scrapy
import os
class GenreSpider(scrapy.Spider):
    name="genre_spider"
    custom_settings = {
        'ITEM_PIPELINES': {
            'anime_scraper.pipelines.GenreScraperPipeline': 400
        }
    }
    start_urls=['https://myanimelist.net/anime.php']

    def parse(self,response):
        genres_container =response.css('.genre-link')[0:4]
        genres = genres_container.css('.genre-name-link')
        rankings=response.css('.genre-link')[5]
        studios=response.css('.genre-link')[4]
        for genre in genres:
            # yield {'genre':genre.css('::text').get()}
            g=genre.css('::text').get().split(' (')[0]
            url=genre.css('::attr(href)').extract()[0]
            g_id=url.split('/')[3]
            yield {'id': g_id,'name': g,'type': 'genre'}
        #     with open("genre.txt", 'a') as f:
        #         f.write(f"name: {g}, id: {g_id}\n")
        # f.close()
        ranking_cats=rankings.css('.genre-name-link')
        for rank in ranking_cats:
            r=rank.css('::text').get().split(' (')[0]
            yield {'id': 1,'name': r, 'type': 'rank'}
        studs=studios.css('.genre-name-link')
        for stud in studs:
            s=stud.css('::text').get().split(' (')[0]
            url=stud.css('::attr(href)').extract()[0]
            id=url.split('/')[3]
            yield {'id': id, 'name': s, 'type': 'studio'}
        
            
        #     for anime in name:
        #         a=anime.split(' (')[0]
        #         print(a)
        #         with open('genres.txt','a') as f:
        #             f.write(f"{anime}\n")
        # f.close()