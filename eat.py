from pymongo import MongoClient

connection = MongoClient("homer.stuy.edu")
db = connection.test
rests = db.restaurants

def get_rests_by_borough(b):
    return rests.find({"borough" : b})

def get_rests_by_zipcode(z):
	return rests.address.find({'zipcode' : str(z)})

def main():
    x = get_rests_by_zipcode(10460)
    for a in x:
        print a

if __name__ == '__main__':
    main()
