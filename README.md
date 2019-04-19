#PythonProject

A project to learn how to use Python with API request.

This application calls the swapi API, a Star Wars database.

This application displays main information of character,species,planet and movie present on the swapi database on web page using flask.


##Information

###Classes

All the 4 main classes (Species,People,Planets,Films) can be launched as main to test the fonctions.

###Json Path

To take the information from the Json, given by the api I use JSON Path ('parse('$..name').find(j)').

But when I saw that we need between 5 and 16 second to open a web page I try to avoid json path using fix path ('j["results"][0]["name"]').

But the loading time hasn't change because its came from the swapi api itself.
