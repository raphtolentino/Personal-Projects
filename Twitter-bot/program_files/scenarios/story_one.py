# library used in this project
import random
import names

# this scenario is about 2 friends going to the high street to buy some clothes.
class scenario_one:
    def scenario_one():
        # dictionaries
        # wedding scenario
        wedding_outfit = {
            "wedding_shirt": "a White formal suit shirt",
            "wedding_tie": "a Black formal suit tie",
            "wedding_shoes": "a pair of Black formal shoes",
            "wedding_suit": "a Black formal suit",
        }
        wedding_lol = {
            "wedding_lol1": "Mark and Spencer",
            "wedding_lol2": "ASOS",
        }

        # gym scenario
        gym_outfit = {
            "gym_shirt": "a red sweatshirt",
            "gym_shorts": "a pair of black shorts",
            "gym_shoes": "a pair of black trainers",
            "gym accessories": "a pair of black gloves",
        }
        gym_lol = {
            "gym_lol1": "JD Sports",
            "gym_lol2": "Nike",
        }
        gym_price = {
            "gym_out1": 50.00,
            "gym_out2": 60.00,
        }
        # joins the gym variables together

        # casual scenario
        casual_outfit = {
            "casual_shirt": "a white t-shirt",
            "casual_trousers": "a pair of black jeans",
            "casual_shoes": "a pair of black trainers",
            "casual accessories": "a black smart watch",
        }
        casual_lol = {
            "casual_lol1": "Topman",
            "casual_lol2": "Zara",
        }
        casual_price = {
            "casual_out1": 40.00,
            "casual_out2": 50.00,
        }
        # random the prices
        wedding_price1 = random.choice(
            [
                wedding_outfit1 = {80.00}
                wedding_outfit2 = {90.00} 
            ]
        )
        gym_price1 = random.choice(
            [
                gym_outfit["gym_out1"],
                gym_outfit["gym_out2"],
            ]
        )
        casual_price1 = random.choice(
            [
                casual_outfit["casual_out1"],
                casual_outfit["casual_out2"],
            ]
        )
        # random the locations
        wedding_lol1 = random.choice(
            [
                wedding_outfit["wedding_lol1"],
                wedding_outfit["wedding_lol2"],
            ]
        )
        gym_lol1 = random.choice(
            [
                gym_outfit["gym_lol1"],
                gym_outfit["gym_lol2"],
            ]
        )
        casual_lol1 = random.choice(
            [
                casual_outfit["casual_lol1"],
                casual_outfit["casual_lol2"],
            ]
        )
        # joins the weddings variables together
        wedding_fit = [
            wedding_outfit["wedding_shirt"],
            wedding_outfit["wedding_tie"],
            wedding_outfit["wedding_shoes"],
            wedding_outfit["wedding_suit"],
            wedding_lol1,
            wedding_price1,
        ]
        # joins the gym variables together
        gym_fit = [
            gym_outfit["gym_shirt"],
            gym_outfit["gym_shorts"],
            gym_outfit["gym_shoes"],
            gym_outfit["gym accessories"],
            gym_lol1,
            gym_price1,
        ]
        # joins the casual variables together
        casual_fit = [
            casual_outfit["casual_shirt"],
            casual_outfit["casual_trousers"],
            casual_outfit["casual_shoes"],
            casual_outfit["casual accessories"],
            casual_lol1,
            casual_price1,
        ]

        # randomize the scenarios
        story = random.choice([wedding_fit, gym_fit, casual_fit])
    # friend system
        friend_zero = names.get_first_name()  # protrag
        friend_one = names.get_first_name()  # friend one
        friend_two = names.get_first_name()  # friend two
    # story variables
        # wedding
        wedding_story = (
            "Today, I went to my local high street to buy an outfit for my friend wedding. "
            + "I met my friend " + friend_zero + " at the high street. "
            + "We went to " + story[4] + " to buy the outfit. "
        )
        
        print(wedding_story)
        
    scenario_one()