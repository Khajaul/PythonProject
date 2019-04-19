# -*-coding:utf-8 -*
# people.py

from flask import Flask, render_template
from jsonpath_rw import jsonpath, parse
import requests
import json
import random

if __name__ == '__main__':
    from StarWars import StarWars
else:
    from classes.StarWars import StarWars

class People(StarWars):
    """Class caracteristics
    - name ;
    - gender ;
    - homeworld ;
    - films ;
    - species;
    - url"""

    
    def __init__(self, name = None):
        """Class constructor"""
        if(name != None):
            request = requests.get('https://swapi.co/api/people/?search={0}'.format(name))
        else:
            request = requests.get('https://swapi.co/api/people/')
            js = json.loads(request.text)
            path = parse('$..count')
            request = requests.get('https://swapi.co/api/people/{0}'.format(random.randint(1,int([match.value for match in path.find(js)][0]))))
        j = json.loads(request.text)
        
        self.name = j["results"][0]["name"]
        
        self.gender = j["results"][0]["gender"]
		
        self.homeworld = StarWars.get_Planets_name(j["results"][0]["homeworld"])
		
        self.films = []
        for element in j["results"][0]["films"]:
            self.films.append(StarWars.get_Films_title(element))
        
        if(j["results"][0]["species"]!=[]):
            self.species = StarWars.get_Species_name(j["results"][0]["species"][0])
        else:
            self.species='Unknown'
        
        self.url = j["results"][0]["url"]
        
    def __repr__(self):
        """Class representation"""
        return "People : {},\n         gender : {}\n         homeworld : {}\n         films : {}\n         specie : {}".format(self.name,self.gender,self.homeworld,self.films,self.species)
        
if __name__ == '__main__':
    people1 = People()
    people2 = People('Yoda')
    print('Test without given title\n')
    print(people1)
    print('\nTest with given title (Yoda)\n')
    print(people2)