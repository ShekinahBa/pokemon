# pokemon
Code First Girl Project

Intro
I had a lot of fun with this project, I really enjoyed expanding the capabilities of this game and learning how to do so with Google & YouTube. The feeling of making it work was unbeatable.

We were given 3 projects to choose from and I wanted to do this (working with an API) and the 3rd project working with CSV files, so I combined the two.

Here is the project Brief:

Project Brief: Top Trumps
In this project you'll create a small game where players compare stats, similar to the Top Trumps
card game. The basic flow of the games is:
1. You are given a random card with different stats
2. You select one of the card's stats
3. Another random card is selected for your opponent (the computer)
4. The stats of the two cards are compared
5. The player with the stat higher than their opponent wins
The standard project will use the Pokemon API, but you can use a different API if you want after
completing the required tasks.
You will not need any additional knowledge beyond what is covered in this course to complete this
project.

Required Tasks
These are the required tasks for this project. You should aim to complete these tasks before
adding your own ideas to the project.
1. Generate a random number between 1 and 151 to use as the Pokemon ID number
2. Using the Pokemon API get a Pokemon based on its ID number
3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★
https://pokeapi.co/)
4. Get a random Pokemon for the player and another for their opponent
5. Ask the user which stat they want to use (id, height or weight)
6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

Ideas for Extending the Project
Here are a few ideas for extending the project beyond the required tasks. These ideas are just
suggestions, feel free to come up with your own ideas and extend the program however you want.
● Use different stats for the Pokemon from the API
● Get multiple random Pokemon and let the player decide which one that they want to use
● Play multiple rounds and record the outcome of each round. The player with most number
of rounds won, wins the game
● Allow the opponent (computer) to choose a stat that they would like to compare

● Record high scores for players and store them in a file
● Use a different API (see suggestions below)

Useful Resources
Harry Potter API
● Homepage ★ https://hp-api.herokuapp.com/
Star Wars API
● Homepage ★ https://swapi.co/
● Documentation ★ https://swapi.co/documentation
Anime/Manga API
● Homepage ★ jikan.moe/
● Documentation ★ jikan.docs.apiary.io
● Example API url ★ https://api.jikan.moe/v3/anime/5

Example Project Code
In this section you will find some example code to complete the required tasks. You can use this
code for guidance if you are finding it difficult to complete the required tasks for this project.
import random
import requests

def random_pokemon():
pokemon_number = random.randint(1, 151)
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()
return {
'name': pokemon['name'],
'id': pokemon['id'],
'height': pokemon['height'],
'weight': pokemon['weight'],
}

def run():
