# library used in this project
import random
import names

# this scenario is about 2 friends having takeaway and a movie night together.
class scenario_three:
    def scenario_three():
        # dictionaries
        takeaway = {
            "take1": "Chinese meal",
            "take2": "American meal",
            "take3": "Pizza meal",
        }
        # locations
        take1_place = {
            "take1_place1": "Wagamama",
            "take1_place2": "Bab Ramen",
        }
        take2_place = {
            "take2_place1": "McDonald's",
            "take2_place2": "Shake Shack",
        }
        take3_place = {
            "take3_place1": "Pizza Hut",
            "take3_place2": "Papa John's",
        }
        # prices
        take1_price = {
            "take1_price1": 10.00,
            "take1_price2": 15.00,
            "take1_price3": 20.00,
        }
        take2_price = {
            "take2_price1": 10.00,
            "take2_price2": 15.00,
            "take2_price3": 20.00,
        }
        take3_price = {
            "take3_price1": 15.00,
            "take3_price2": 20.00,
            "take3_price3": 25.00,
        }
        # randomizer for the dinner
        # Chinese meal
        takeaway1_price = random.choice(
            [
                take1_price["take1_price1"],
                take1_price["take1_price2"],
                take1_price["take1_price3"],
            ]
        )
        takeaway1 = [takeaway["take1"], take1_place["take1_place1"], takeaway1_price]

        # American meal
        takeaway2_price = random.choice(
            [
                take2_price["take2_price1"],
                take2_price["take2_price2"],
                take2_price["take2_price3"],
            ]
        )
        takeaway2 = [takeaway["take2"], take2_place["take2_place1"], takeaway2_price]
        # Pizza meal
        takeaway3_price = random.choice(
            [
                take3_price["take3_price1"],
                take3_price["take3_price2"],
                take3_price["take3_price3"],
            ]
        )
        takeaway3 = [takeaway["take3"], take3_place["take3_place1"], takeaway3_price]
        # randomize the meal variable
        takeaway_final = random.choice([takeaway1, takeaway2, takeaway3])
        # friend system
        friend_zero = names.get_first_name()  # protrag
        friend_one = names.get_first_name()  # friend one
        friend_two = names.get_first_name()  # friend two

        # movie system
        movie = {
            "mov1": "The Lion King",
            "mov2": "Avatar 2",
            "mov3": "Everything, Everwhere all at Once",
        }
        # randomize the movie variable
        movie_final = random.choice([movie["mov1"], movie["mov2"], movie["mov3"]])

        # story variable
        scenario_three_story = (
            "Today, I went over to my friend "
            + friend_one
            + "'s house for a movie night. We ordered the "
            + takeaway_final[0]
            + " from the local "
            + takeaway_final[1]
            + " and watched "
            + movie_final
            + " in her living room. It was a great night"
            + "."
            + " I hope we get to invite "
            + friend_two
            + " next."
        )
        # print the story and story length
        print(scenario_three_story)
        
        # if length of the story is less than 240 characters, print OK for twitter otherwise print too long
        if len(scenario_three_story) < 240:
            print("OK for twitter")
        else:
            print("Too long for twitter")
    scenario_three()
