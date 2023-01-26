# import scenarios from another folder
import sys
import random
# add the scenario and output folders to the system path
sys.path.insert(0,'/scenarios')

# import functions from the folders
# -- scenario one -- 
from scenarios.story_one import scenario_one # import scenario_one and the class
# -- scenario two -- 
from scenarios.scenario_two import scenario_two # import scenario class from the folder 
# -- scenario three -- 
from scenarios.scenario_three import scenario_three # import scenario class from the folder
# -- scenario four --

# adapt the function into variables for this file

scenario_one = scenario_one
scenario_two = scenario_two
scenario_three = scenario_three

# print the variables and length of the variables
print(scenario_one)
print(scenario_two)
print(scenario_three)

# randomize the scenarios and print them into a file
story = random.choice([scenario_one, scenario_two])
# print the story
print(story)

# saves the reference of the standard output
original_stdout = sys.stdout

with open('output.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(story) # Prints the story to a file.
    print('This message will be written to a file.')
    sys.stdout = original_stdout # Reset the standard output to its original value
    print('This message will be written to the console.')

