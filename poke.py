# Team PokeMongo

'''
The data we are using is from pokeapi.co. It is a list of all the pokemon and their stats and abilities.
'''

import urllib2, json

from pymongo import MongoClient

connection = MongoClient("homer.stuy.edu")
db = connection.PokeMongo


def get_pokemon_data(pid):
  url = urllib2.urlopen('https://pokeapi.co/api/v2/pokemon/' + str(pid))
  return url.read()


def insert_pokemon():
  pass


def main():
  print get_pokemon_data(1)


if __name__ == '__main__':
  main()
