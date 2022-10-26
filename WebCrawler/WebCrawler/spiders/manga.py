import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsMangaItem
import time
import string


class MangaSpider(scrapy.Spider):
    name = 'manga'
    allowed_domains = ['myanimelist.net']
    start_urls = ['http://myanimelist.net/']

    def start_requests(self):
        alphabet = list(string.ascii_uppercase)
        start_urls = [f'https://myanimelist.net/manga.php?letter={alphabet}'for alphabet in alphabet]
        for url in start_urls:
            yield Request(url=url, callback=self.parse_manga)


    def parse_manga(self, response):
        liste_manga = response.css('tr')[9:] #On enlève les 9 premières lignes qui ne sont pas des mangas

        for manga in liste_manga:
            item = ReviewsMangaItem()
            #indice boursier
            try: 
              item['img'] = manga.css('img').attrib['data-src']
            except:
              item['img'] = 'None'
            
            #indice cours de l'action
            try: 
              item['desc'] = manga.css('div.pt4::text')[0].extract()
            except:item['desc'] = 'None'
            
            # #Variation de l'action 
            try: 
              item['title'] = manga.css('a.hoverinfo_trigger.fw-b').css('strong::text').extract()
            except:
              item['title'] = 'None'
            
            yield item
      

