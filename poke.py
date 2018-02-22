# Team PokeMongo

'''
The data we are using is from pokeapi.co. It is a list of all the pokemon and their stats and abilities. We will be storing this information for the 1st 151 pokemon in the database.
command line argument examples:
python poke.py has_type grass

run with no command line arguments for list of commands
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

def has_type(_type):
	return db.pokemons.find({'types.type.name' : _type})

def get_types(poke):
	types = []
	for type in poke['types']:
		types.append(type['type']['name'])
	if(poke['types'][0]['slot'] == 2):
		tmp = types[0]
		types[0] = types[1]
		types[1] = tmp
	return types

def main():
	if(len(sys.argv) <= 1):
		print "not enough arguments"
		print "args"
		print "-----"
		print "upload_db - imports the dataset"
		print "heavier_than <weight> - gets every pokemon heavier than <weight>"
		print "lighter_than <weight> - gets every pokemon lighter than <weight>"
		print "has_type <type> - gets every pokemon with that type"
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
	elif(sys.argv[1] == "has_type"):
		c = has_type(sys.argv[2])
		for i in c:
			print i['name'] + ' : ' + str(get_types(i))


if __name__ == '__main__':
  main()
