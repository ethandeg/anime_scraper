# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class AnimeScraperLinkItem(scrapy.Item):
    link=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GenreScraperItem(scrapy.Item):
    name=scrapy.Field()
    id=scrapy.Field()

