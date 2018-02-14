from pymongo import MongoClient

connection = MongoClient("homer.stuy.edu")
db = connection.test
rests = db.restaurants

def get_rests_by_borough(b):
    return rests.find({"borough" : b})

def get_rests_by_zipcode(z):
	return rests.find({'address.zipcode' : str(z)})

def get_rests_by_zipcode_and_grade(z,g):
	return rests.find({'address.zipcode' : str(z), 'grades.grade' : str(g)})

def get_rests_by_zipcode_and_score_below_a_specific_threshold(z,t):
	return rests.find({'address.zipcode' : str(z), 'grades.0.score' : {'$lt' : t}})

def get_rests_with_score_above_a_specific_threshold_or_with_a_specific_score(t,s):
	return rests.find({'$or' : [{'grades.0.score' : {'$gt' : t}},{'grades.0.score' : s}]})

def main():
    x = get_rests_with_score_above_a_specific_threshold_or_with_a_specific_score(5,2)
    for a in x:
        print a

if __name__ == '__main__':
    main()
