from re import A
import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsAllocineItem


class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['www.allocine.fr']
    
    #Liste des pages à collecter
    


    def start_requests(self):
        nb = int(input("Enter the size of list : "))
        print(nb)

        # start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1,20)]
        start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1,nb+1)]
        print(start_urls)
        for url in start_urls:
            
            yield Request(url=url, callback=self.parse_film)
        
        
    def parse_film(self, response):
        liste_film = response.css('li.mdl')
        
        
        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = film.css('a.meta-title-link::text')[0].extract()
            except:
                item['title'] = 'None'
              
            # Lien de l'image du film
            try:
                # item['img'] = film.css('img').attrib['src'].extract()
                item['img'] = film.css('li.mdl').css('img').attrib['src']
            except:
                item['img'] = 'None'


            # Auteur du film
            try:
                item['author'] = film.css('a.blue-link::text')[0].extract()
            except:
                item['author'] = 'None'
           
            # Durée du film
            try:
                item['time'] = film.css('div.meta-body-item.meta-body-info::text')[0].extract().strip('\n')
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = film.css('.meta-body-item.meta-body-info')[0].css('span::text')[1:4].extract()
            except:
                 item['genre'] = 'None'

            # Score du film
            try:
                item['score'] = film.css('span.stareval-note::text')[0:2].extract()
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = film.css('div.content-txt::text').extract().strip()
            except:
                item['desc'] = 'None'

            # Date de sortie
            try:
                item['release'] = film.css('span.light::text')[0].extract()
                if(item['release'] != 'Date de reprise'):
                    item['release'] = 'None'    
                else :
                    item['release'] = film.css('span.date::text').extract()
                # item['release'] = film.css('div.meta-body-item::text')[0].extract()
            except:
                item['release'] = 'None'


            yield item