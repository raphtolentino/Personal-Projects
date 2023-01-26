# libraries used in this project
# import pytest
import random
import names

# this scenario is about 3 friends visiting the cinema together and part-taking in an activity together.
# pytest function
class scenario_two:
    def scenario_two():
        # dictionaries
        cinema_lol = {
            "lol1": "Cinema located in my high street",
            "lol2": "Cinema located in Central London",
            "lol3": "Cinema in the West End",
        }
        cinema_act = {
            "act1": "a long walk",
            "act2": "coffee",
            "act3": "Boba Tea",
            "act4": "Burger meal",
        }
        cinema_movie = {
            "mov1": "The Lion King",
            "mov2": "Avatar 2",
            "mov3": "Everything, Everwhere all at Once",
        }
        # randomise all dictionary
        cinema_final_lol = random.choice(list(cinema_lol.items()))
        cinama_final_act = random.choice(list(cinema_act.items()))
        cinema_final_movie = random.choice(list(cinema_movie.items()))
        # prices and calculations
        ticket_price = 10.00
        ticket_discount = ticket_price * 0.15
        # meals
        s_meal = 12.00
        m_meal = 15.00
        l_meal = 18.00

        # randomize the meal variable
        cinema_final_meal = random.choice([s_meal, m_meal, l_meal])
        # calculation
        ticket_final = ticket_discount + cinema_final_meal
        ticket_final_format = " £ " + "{:.2f}".format(ticket_final)

        # friend system
        friend_zero = names.get_first_name()  # protrag
        friend_one = names.get_first_name()  # friend one
        friend_two = names.get_first_name()  # friend two

        # story variable about going to the cinema and part-taking in an activity with the total with 2 friends
        scenario_two_story = (
            "Today I went to the cinema with "  # story start
            + friend_one
            + " and "
            + friend_two
            + " to watch "
            + cinema_final_movie[1]
            + " at "
            + cinema_final_lol[1]
            + " and we went for "
            + cinama_final_act[1]
            + " afterwards. "
            + "The total cost of the cinema ticket was "
            + ticket_final_format
            + " and the total cost of the "
            + cinama_final_act[1] # activity
            + " was "
            + " £ "
            + "{:.2f}".format(cinema_final_meal)
            + "."
        )
        print(scenario_two_story)
         # if length of the story is less than 240 characters, print OK for twitter otherwise print too long
        if len(scenario_two_story) < 240:
            print("OK for twitter")
        else:
            print("Too long for twitter")
    scenario_two()
