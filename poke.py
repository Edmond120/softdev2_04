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

def heavier_than(weight):
	return db.pokemons.find({ "weight" : { "$gt" : weight } })

def lighter_than(weight):
	return db.pokemons.find({ "weight" : { "$lt" : weight } })

def main():
	if(len(sys.argv) <= 1):
		print "not enough arguments"
		print "args"
		print "-----"
		print "upload_db - imports the dataset"
		print "heavier_than <weight> - gets every pokemon heavier than <weight>"
		print "lighter_than <weight> - gets every pokemon lighter than <weight>"
	elif(sys.argv[1] == "upload_db"):
		x = 1
		while(x <= 151):
			insert_pokemon(x)
			x += 1
	elif(sys.argv[1] == "heavier_than"):
		c = heavier_than(int(sys.argv[2]))
		for i in c:
			print i['name'] + ' : ' + str(i['weight'])
	elif(sys.argv[1] == "lighter_than"):
		c = lighter_than(int(sys.argv[2]))
		for i in c:
			print i['name'] + ' : ' + str(i['weight'])


if __name__ == '__main__':
  main()
