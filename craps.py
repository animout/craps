####
#  Author: JustinRuth
#  Title: TheHardWayEx43
#  Description: text based game. - street craps
####


import sys
#random number generation
from random import randint


#Rules String
"""Welcome to street craps!  At the start of the game you will roll 2 dice,
   7, 11 instantly win
   double 1s, double 12s, or 3 instantly lose.
   Any other number establishes a point.  
   Once a point is established roll it again before a 7 in order to win.
"""

#TODO 
#welcome member to the game, create quit or roll inputs.
#Create flag to determine if the point is established or not.
#Create crap numbers
#Create Win numbers.
#create roll action (random number generatorx2 1 through 6)
#Print the roll results to the member.

#################global variables###########3
#container for rule set.
rules = """7, 11 instantly win
        double 1's, double 12's, or 3 instantly lose.
        Any other number establishes a point.  
        Once a point is established roll it again before a 7 
        in order to win.
        """


#losing numbers before point is established         
comeout_crap_numbers = [2, 3, 12]

#wining numbers before point is established
comeout_win_numbers = [7, 11]

#losing numbers after point is established
point_established_losing_numbers = [7]


#Function to welcome user to game and print introduction
def welcome():
    print('Hello!!!! Welcome to Street Craps!\nWhen ready type "start" to start the game and if you require a refresher type "rules".\nAt anytime type "exit" to quit. Enjoy!')
    
    #ask user for an input through the function.
    input()
    

#Function to indicate when user wins
def win():
    pass

#Function to indicate when user loses
def lose():
    pass 

#Function to exit game
def quit():
    print('Exiting...')
    exit()

 
#function to capture users input.  
def input():
    user_input = raw_input('start, rules, or quit,: ')

    #if user types quit, call quit
    if user_input.lower() =='quit':
        quit()
    #if user types rules, print rules.  
    elif user_input.lower() == 'rules':    
        #print rules 
        print(rules)
        input()
    
    #if user types roll, call roll
    if user_input.lower() == 'start':
        start()

        #ask user for input again.
        
    else:
        print('invalid input')

        #ask user for input again.
        input()

def start():
#point value set the 0 because game is just starting
    point = 0
    
    def roll(point):
        print ("rolling...rolling....rolling....")

        #dice one random number 
        die_1 = randint(1,6)
        print ("Die 1 stops at a:", die_1)
    

        #dice two random number 
        die_2 = randint(1,6)
        print ("Die 2 stops at a:", die_2)

        #score
        score = (die_1 + die_2)
        print ("you rolled a:", score)


        if point == 0:
            if score in comeout_crap_numbers:
                print("call lose on comeout")  
            elif score in comeout_win_numbers:
                print("call win on comeout")
            else:    
                point = score
                print ("point now set at:", point)
                roll(point)
                
        elif score in point_established_losing_numbers:
            print("call you lose")
        elif score == point:
            print("call you win")
        else:
            roll(point)
    roll(point)
    
#on program run call welcome function
welcome()