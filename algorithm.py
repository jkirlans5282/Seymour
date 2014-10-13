#Algorithm Test

users = {
"Tom":{"A":1,"B":1,"C":0,"D":-1,"H":1,"F":1},
"Beth":{"A":1,"D":-1,"E":1},
"Mike":{"B":1,"E":1,"H":1},
"Emma":{"D":1,"G":0,"E":1}
}

def addUser(username):
    users[username]={}

def addRestaurant(restaurant,username):
    preference = raw_input("[F]avorite, [L]iked, [D]isliked?  ")
    if preference == "F":
        preference = 1
    elif preference == "L":
        preference = 0
    elif preference == "D":
        preference = -1
    temp = users[username]
    temp[restaurant] = preference
    users[username] = temp

def userMatch(username):
    matchscore = {}
    for key in users:
        if key != username:
            name = key
            temp = users[key]
            user = users[username]
            matchscore[name] = 0
            for key in temp:
                try:
                    matchscore[name] = matchscore[name] + (1 * temp[key] * user[key])
                except KeyError:
                    print("")
    print(matchscore)
    reccommend(matchscore)
              
def reccommend(matchscore):
    restaurants = {}
    for key in matchscore:
        name = key
        weight = matchscore[key]
        ratings = users[key]
        for key in ratings:
            try:
                restaurants[key] = restaurants[key] + weight * ratings[key]
            except KeyError:
                restaurants[key] = weight
    print(restaurants)
            


def main():
    while True:
        navigate = raw_input("[N]ew user, [R]ate restaurant, [P]rint info, [M]atch users, [Q]uit?  ")
        if navigate == "N":
            username = raw_input("Username?  ")
            addUser(username)
        elif navigate == "R":
            username = raw_input("Username?  ")
            restaurant = raw_input("Restaurant?  ")
            addRestaurant(restaurant,username)
        elif navigate == "P":
            print(users)
        elif navigate == "M":
            username = raw_input("Username?  ")
            userMatch(username)
        elif navigate == "Q":
            False

main()
