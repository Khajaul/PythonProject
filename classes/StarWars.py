# -*-coding:utf-8 -*
# people.py

from flask import Flask, render_template
from jsonpath_rw import jsonpath, parse
import requests
import json

class StarWars:
        
    def get_People_name(url):
        request = requests.get(url)
        js = json.loads(request.text)
        #path = parse('$..name')
        #return [match.value for match in path.find(js)][0]
        return js["name"]
    
    def get_Planets_name(url):
        request = requests.get(url)
        js = json.loads(request.text)
        #path = parse('$..name')
        #return [match.value for match in path.find(js)][0]
        return js["name"]
    
    def get_Species_name(url):
        request = requests.get(url)
        js = json.loads(request.text)
        #path = parse('$..name')
        #return [match.value for match in path.find(js)][0]
        return js["name"]
        
    def get_Films_title(url):
        request = requests.get(url)
        js = json.loads(request.text)
        #path = parse('$..title')
        #return [match.value for match in path.find(js)][0]
        return js["title"]