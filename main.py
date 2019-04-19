# -*-coding:utf-8 -*
# main.py

from flask import Flask, render_template
from jsonpath_rw import jsonpath, parse
import requests
import json
from classes.People import People
from classes.Films import Films
from classes.Species import Species
from classes.Planets import Planets

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  r = requests.get('https://swapi.co/api/films/')
  j = json.loads(r.text)
  path = parse('$..title')
  movies = [match.value for match in path.find(j)]
  r = requests.get('https://swapi.co/api/planets/')
  j = json.loads(r.text)
  path = parse('$..name')
  planets = [match.value for match in path.find(j)]
  r = requests.get('https://swapi.co/api/people/')
  j = json.loads(r.text)
  path = parse('$..name')
  people = [match.value for match in path.find(j)]
  r = requests.get('https://swapi.co/api/species/')
  j = json.loads(r.text)
  path = parse('$..name')
  species = [match.value for match in path.find(j)]
  return render_template('templates/main.html', movies = movies,planets = planets,people = people,specie = species ) 

@app.route('/people/<name>')
def people(name=None):
    if(name!=None):
        people = People(name = name)
        return render_template('templates/People.html', name=people.name, gender = people.gender, homeworld=people.homeworld, specie = people.species, movies = people.films)
    else:
        return redirect(url_for('homepage'))
    
@app.route('/movies/<title>')
def movies(title=None):
    if(title!=None):
        movie = Films(title = title)
        return render_template('templates/Movies.html', title=movie.title, director = movie.director, producer = movie.producer, characters = movie.characters, planets=movie.planets, species=movie.species, resume=movie.resume)
    else:
        return redirect(url_for('homepage'))
		
@app.route('/species/<name>')
def species(name=None):
    if(name!=None):
        specie = Species(name = name)
        return render_template('templates/Species.html', name=specie.name, language=specie.language,homeworld=specie.homeworld,movies=specie.films, people = specie.people)
    else:
        return redirect(url_for('homepage'))
		
@app.route('/planets/<name>')
def planets(name=None):
    if(name!=None):
        planet = Planets(name = name)
        return render_template('templates/Planets.html', name=planet.name, climate=planet.climate,population=planet.population,terrain=planet.terrain, movies=planet.films, residents = planet.residents)
    else:
        return redirect(url_for('homepage'))
    
if __name__ == '__main__':
    app.run(debug=True)
