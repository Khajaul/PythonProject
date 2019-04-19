# -*-coding:utf-8 -*
# planets.py

from flask import Flask, render_template
from jsonpath_rw import jsonpath, parse
import requests
import json
import random

if __name__ == '__main__':
    from StarWars import StarWars
else:
    from classes.StarWars import StarWars
	
class Planets(StarWars):
    """Class caracteristics
    - name ;
    - climate ;
    - population ;
    - terrain ;
    - films ;
    - residents ;
    - url"""

    
    def __init__(self, name = None):
        """Class constructor"""
        if(name != None):
            request = requests.get('https://swapi.co/api/planets/?search={0}'.format(name))
        else:
            request = requests.get('https://swapi.co/api/planets/')
            js = json.loads(request.text)
            path = parse('$..count')
            request = requests.get('https://swapi.co/api/planets/{0}'.format(random.randint(1,int([match.value for match in path.find(js)][0]))))
        j = json.loads(request.text)
        
        self.name = j["results"][0]["name"]
        
        self.climate = j["results"][0]["climate"]
        
        self.population = j["results"][0]["population"]
        
        self.terrain = j["results"][0]["terrain"]

        self.films = []
        for element in j["results"][0]["films"]:
            self.films.append(StarWars.get_Films_title(element))
        
        self.residents = []
        for element in j["results"][0]["residents"]:
            self.residents.append(StarWars.get_People_name(element))
            
        self.url = j["results"][0]["url"]
        
        
    def __repr__(self):
        """Class representation"""
        return "Planet : {},\n         climate : {}\n         population : {}\n         terrain : {}\n         films : {}\n         residents : {}".format(self.name,self.climate,self.population,self.terrain,self.films,self.residents)

if __name__ == '__main__':
    planet1 = Planets()
    planet2 = Planets('Yavin')
    print('Test without given title\n')
    print(planet1)
    print('\nTest with given title (Yavin)\n')
    print(planet2)