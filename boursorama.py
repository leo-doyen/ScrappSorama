from re import A
import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursoramaItem
import time
import datetime

class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['www.boursorama.com']
   

    def start_requests(self):
        start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}/?france_filter[market]=1rPCAC' for n in range(1,3)]

        for url in start_urls:
            yield Request(url=url, callback=self.parse_boursorama)
            
    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]
        
        for indices in liste_indices:
            item = ReviewsBoursoramaItem()
            
            #indice boursier
            try: 
              item['indice'] = indices.css('a.c-link::text').get()
            except:
              item['indice'] = 'None'
            
            #indice cours de l'action
            try: 
              item['cours'] = indices.css('span.c-instrument--last::text')[0].extract()
            except:item['cours'] = 'None'
            
            # #Variation de l'action 
            try: 
              item['var'] = indices.css('span.c-instrument--instant-variation::text')[0].extract()
            except:
              item['var'] = 'None'
            
            # #Valeur la plus haute 
            try: 
              item['hight'] = indices.css('span.c-instrument--high::text')[0].extract()
            except:
              item['hight'] = 'None'
            
            # #Valeur la plus basse 
            try: 
              item['low'] = indices.css('span.c-instrument--low::text')[0].extract()
            except:
              item['low'] = 'None'

            # #Valeur d'ouverture
            try: 
              item['open_'] = indices.css('span.c-instrument.c-instrument--open::text')[0].extract()
            except:
              item['open_'] = 'None'

            # #Date de la collecte
            try: 
              item['time'] =  datetime.datetime.now()
            except:
              item['time'] = 'None'

            
            yield item