import scrapy
import os
import sys
class AnimeSpider(scrapy.Spider):
    name="anime_spider"
    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'anime_scraper.pipelines.GenreScraperPipeline': 400
    #     }
    # }
    start_urls=['https://myanimelist.net/anime.php']
    custom_settings = {
        'ITEM_PIPELINES': {
            'anime_scraper.pipelines.AnimeLinkScraperPipeline': 400
        }
    }


    def parse(self,response):
        if os.path.exists('links.txt'):
            os.remove('links.txt')
        if os.path.exists('parentlinks.txt'):
            os.remove('parentlinks.txt')
        if os.path.exists('grandparentlinks.txt'):
            os.remove('grandparentlinks.txt')
        nav=response.css('#horiznav_nav')
        all_links=nav.css('ul > li > a::attr(href)').getall()
        anime_links=[i for i in all_links if 'letter=' in i]
        anime_links=list(set(anime_links))
        for link in anime_links:
            with open('grandparentlinks.txt','a',encoding='utf-8') as f:
                f.write(f"{link}\n")
            # headers = {'User-Agent': 'gitMozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
            yield scrapy.Request(link,self.get_pages)
        
            # print(f'{link}*********')
        f.close()
    
    def get_pages(self,response,visited_urls=[]):
        # index=int(response.css('span.bgColor1 > a::text').get())
        all_links=list(set(response.css('span.bgColor1 > a::attr(href)').getall()))

        for link in all_links:
            link=response.urljoin(link)
            if link not in visited_urls:
                with open('parentlinks.txt','a',encoding='utf-8') as f:
                    f.write(f"{link}\n")
                    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
                    visited_urls.append(link)
                    yield {'link': link, 'type': 'url'}
                    yield scrapy.Request(link,self.get_pages)
                    # print(f'{link}1111111111')
        # for url in visited_urls:
        #     # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        #     yield scrapy.Request(url,self.parse_anime_url)
        
        # f.close()
        # all_links.append(response.url)
        # all_links=list(set(all_links))
        # for link in all_links:
        #     link=response.urljoin(link)
        #     with open('parentlinks.txt','a',encoding='utf-8') as f:
        #         f.write(f'{link}\n')
        #     yield scrapy.Request(link,self.parse_anime_url)
        # f.close()

    def parse_anime_url(self,response):
        anime_links=list(set(response.css('a.hoverinfo_trigger::attr(href)').getall()))
        print('MADE IT')
        for link in anime_links:
            with open('links.txt','a',encoding='utf-8') as f:
                f.write(f"{link}\n")
        f.close()
