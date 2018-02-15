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

def print5(restaurants):
    ctr = 0
    for r in restaurants:
        print r
        ctr+=1
        if ctr > 5:
            break


def main():
    raw_input("\nPress enter to get 5 restaurants in the borough of Manhattan\n")
    restaurants = get_rests_by_borough('Manhattan')
    print5(restaurants)

    raw_input("\nPress enter to get 5 restaurants with the zipcode 10460\n")
    restaurants = get_rests_by_zipcode(10460)
    print5(restaurants)

    raw_input("\nPress enter to get 5 restaurants with the zipcode 10460 and a grade of A\n")
    restaurants = get_rests_by_zipcode_and_grade(10460, 'A')
    print5(restaurants)

    raw_input("\nPress enter to get 5 restaurants with the zipcode 10460 and a score of 7 or below\n")
    restaurants = get_rests_by_zipcode_and_score_below_a_specific_threshold(10460, 7)
    print5(restaurants)

    raw_input("\nPress enter to get 5 restaurants with a score greater than 5 or EXACTLY 2\n")
    restaurants = get_rests_with_score_above_a_specific_threshold_or_with_a_specific_score(5,2)
    print5(restaurants)


if __name__ == '__main__':
    main()
