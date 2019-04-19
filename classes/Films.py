# -*-coding:utf-8 -*
# films.py

from flask import Flask, render_template
from jsonpath_rw import jsonpath, parse
import requests
import json
import random


if __name__ == '__main__':
    from StarWars import StarWars
else:
    from classes.StarWars import StarWars

class Films(StarWars):
    """Class caracteristics
    - title ;
    - director ;
    - producer ;
    - characters ;
    - planets ;
    - species ;
    - resume ;
    - url"""

    
    def __init__(self, title = None):
        """Class constructor"""
        if(title != None):
            request = requests.get('https://swapi.co/api/films/?search={0}'.format(title))
        else:
            request = requests.get('https://swapi.co/api/films/')
            js = json.loads(request.text)
            path = parse('$..count')
            request = requests.get('https://swapi.co/api/films/{0}'.format(random.randint(1,int([match.value for match in path.find(js)][0]))))
        j = json.loads(request.text)
        
        path = parse('$..title')
        self.title = [match.value for match in path.find(j)][0]
        
        path = parse('$..director')
        self.director = [match.value for match in path.find(j)][0]
        
        path = parse('$..producer')
        self.producer = [match.value for match in path.find(j)][0]
        
        path = parse('$..characters')
        self.characters = []
        for element in [match.value for match in path.find(j)][0]:
            self.characters.append(StarWars.get_People_name(element))
            
        path = parse('$..planets')
        self.planets = []
        for element in [match.value for match in path.find(j)][0]:
            self.planets.append(StarWars.get_Planets_name(element))
            
        path = parse('$..species')
        self.species = []
        for element in [match.value for match in path.find(j)][0]:
            self.species.append(StarWars.get_Species_name(element))
            
        path = parse('$..opening_crawl')
        self.resume = [match.value for match in path.find(j)][0]
        
        path = parse('$..url')
        self.url = [match.value for match in path.find(j)][0]
        
        
    def __repr__(self):
        """Class representation"""
        return "Film : {},\n         director : {}\n         producer : {}\n         characters : {}\n         planets : {}\n         species : {}\n         resume : {}".format(self.title,self.director,self.producer,self.characters,self.planets,self.species,self.resume)
if __name__ == '__main__':
    film1 = Films()
    film2 = Films('Hope')
    print('Test without given title\n')
    print(film1)
    print('\nTest with given title (Hope)\n')
    print(film2)