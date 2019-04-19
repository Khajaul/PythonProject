# -*-coding:utf-8 -*
# species.py

from flask import Flask, render_template
from jsonpath_rw import jsonpath, parse
import requests
import json
import random

if __name__ == '__main__':
    from StarWars import StarWars
else:
    from classes.StarWars import StarWars

class Species(StarWars):
    """Class caracteristics
    - name ;
    - language ;
    - homeworld ;
    - films ;
    - people ;
    - url"""

    
    def __init__(self, name = None):
        """Class constructor"""
        if(name != None):
            request = requests.get('https://swapi.co/api/species/?search={0}'.format(name))
        else:
            request = requests.get('https://swapi.co/api/species/')
            js = json.loads(request.text)
            path = parse('$..count')
            request = requests.get('https://swapi.co/api/species/{0}'.format(random.randint(1,int([match.value for match in path.find(js)][0]))))
        j = json.loads(request.text)
        
        path = parse('$..name')
        self.name = [match.value for match in path.find(j)][0]
        
        path = parse('$..language')
        self.language = [match.value for match in path.find(j)][0]
        
        path = parse('$..homeworld')
        self.homeworld = StarWars.get_Planets_name([match.value for match in path.find(j)][0])

        path = parse('$..films')
        self.films = []
        for element in [match.value for match in path.find(j)][0]:
            self.films.append(StarWars.get_Films_title(element))
			
        path = parse('$..people')
        self.people = []
        for element in [match.value for match in path.find(j)][0]:
            self.people.append(StarWars.get_People_name(element))
            
        path = parse('$..url')
        self.url = [match.value for match in path.find(j)][0]
        

    def __repr__(self):
        """Class representation"""
        return "Specie : {},\n         language : {}\n         homeworld : {}\n         films : {}\n         people : {}".format(self.name,self.language,self.homeworld,self.films,self.people)

if __name__ == '__main__':
    specie1 = Species()
    specie2 = Species('Hutt')
    print('Test without given title\n')
    print(specie1)
    print('\nTest with given title (Hutt)\n')
    print(specie2)