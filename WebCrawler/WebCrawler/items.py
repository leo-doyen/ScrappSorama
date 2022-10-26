# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from platform import release
import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewsBoursoramaItem(scrapy.Item):
    indice = scrapy.Field()
    cours = scrapy.Field()
    var = scrapy.Field()
    hight = scrapy.Field()
    low = scrapy.Field()
    open_ = scrapy.Field()
    time = scrapy.Field()

    pass

class ReviewsAllocineItem(scrapy.Item):
     
     img  = scrapy.Field()
     author = scrapy.Field()
     time = scrapy.Field()
     genre = scrapy.Field()
     score = scrapy.Field()
     desc = scrapy.Field()
     release = scrapy.Field()   

     title = scrapy.Field()
    
     pass