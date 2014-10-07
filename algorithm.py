#Algorithm Test

users = {
"Tom":{"Burgers":1,"Mexican":-1,"Pie":2,"Indian":2,"Italian":2},
"Beth":{"Burgers":1,"Mexican":2,"Pie":2,"Indian":2},
"George":{"Burgers":
}

def addUser(username):
    users[username]={}

def addRestaurant(restaurant,username):
    preference = raw_input("[F]avorite, [L]iked, [D]isliked?  ")
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
                    if temp[key] == "F" and user[key] == "F":
                        matchscore[name] = matchscore[name] + 1
                    elif temp[key] == "D" and user[key] == "F":
                        matchscore[name] = matchscore[name] - 1
                    elif temp[key] == "F" and user[key] == "D":
                        matchscore[name] = matchscore[name] - 1
                    elif temp[key] == "D" and user[key] == "D":
                        matchscore[name] = matchscore[name] + 1
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
            if ratings[key] == "F":
                try:
                    restaurants[key] = restaurants[key] + weight
                except KeyError:
                    restaurants[key] = weight
            elif ratings[key] == "D":
                try:
                    restaurants[key] = restaurants[key] - weight
                except KeyError:
                    restaurants[key] = 0 - weight
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
