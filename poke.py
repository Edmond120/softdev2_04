# Team PokeMongo

'''
The data we are using is from pokeapi.co. It is a list of all the pokemon and their stats and abilities. We will be storing this information for the 1st 151 pokemon in the database.
'''

import urllib2, json, sys
from pymongo import MongoClient

## Some globals
connection = MongoClient("homer.stuy.edu")
db = connection.PokeMongo
api_url = "http://pokeapi.co/api/v2/"


def get_poke_data(num):
    url = api_url + 'pokemon/' + str(num)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    obj = opener.open(url)
    obj = obj.read()
    return json.loads(obj)

def insert_pokemon(num):
	document = get_poke_data(num)
	db.pokemons.insert_one(document)

def main():
	if(len(sys.argv) <= 1):
		print "not enough arguments"
		print "args"
		print "-----"
		print "upload_db - imports the dataset"
	elif(sys.argv[1] == "upload_db"):
		x = 1
		while(x <= 151):
			insert_pokemon(x)
			x += 1


if __name__ == '__main__':
  main()
