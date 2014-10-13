#Algorithm Test

#nested dictionary, {username:{resturant:rating}}
users = {
"tom":{"a":1,"b":1,"c":0,"d":-1,"h":1,"f":1},
"beth":{"a":1,"d":-1,"e":1},
"mike":{"b":1,"e":1,"h":1},
"emma":{"d":1,"g":0,"e":1}
}

def addUser(username):
    users[username]={}

def addRestaurant(restaurant,username):
    while True:
        preference =input("[F]avorite, [L]iked, [D]isliked?  ").lower()
        if preference == "f":
            preference = 1
            break
        elif preference == "l":
            preference = 0
            break
        elif preference == "d":
            preference = -1
            break
        else:
            print("not a vaild option")

    temp = users[username]
    temp[restaurant] = preference
    users[username] = temp


def userMatch(username):
    otherUsersMatchScore = {}
    user = users[username]              # assigns users ratings to user
    for key in users:
        if key != username:             # for all except username, We'll need to change this later to avoid lag once our data set gets larger.
            name = key                  # assigns the username to name
            temp = users[key]           # assigns their ratings to temp
            otherUsersMatchScore[name] = 0        # sets otherUsersMatchScore for the other user initially equal to zero
            for key in temp:            # For resturant rating pairs of the user that isnt the entered username
                try:
                    otherUsersMatchScore[name] = otherUsersMatchScore[name] + (1 * temp[key] * user[key])  # scores the entered users similarity to other users by summing the overlaps in rating. Essentially. (both like it (1,1) adds one to score, one likes other dislikes subtracts one)
                except KeyError:
                    print("keyerror")   # hits this when the User has not also been to the resturant. Essentially does nothing. 
    print(otherUsersMatchScore)
    reccommend(otherUsersMatchScore)
              
def reccommend(otherUsersMatchScore):
    restaurants = {}
    for key in otherUsersMatchScore:
        name = key
        weight = otherUsersMatchScore[key]
        ratings = users[key] #looks at their ratings
        for key in ratings:
            try:
                restaurants[key] = restaurants[key] + weight * ratings[key]
            except KeyError:                                                    # catch key error, and value it = weight? why? will it ever hit this?
                print("Rkeyerror")
                restaurants[key] = weight
    print(restaurants)
            
def main():
    while True:
        navigate =input("[N]ew user, [R]ate restaurant, [P]rint info, [M]atch users, [Q]uit?  ").lower()
        if navigate == "n":
            username =input("Username?  ").lower
            addUser(username)
        elif navigate == "r":
            username =input("Username?  ").lower()
            restaurant =input("Restaurant?  ").lower()
            addRestaurant(restaurant,username)
        elif navigate == "p":
            print(users)
        elif navigate == "m":
            username =input("Username?  ").lower()
            userMatch(username)
        elif navigate == "q":
            break
        else:
            print("Not a valid input value")
main()