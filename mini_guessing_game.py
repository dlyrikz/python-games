# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

# initialize global variables used in your code
low = 0
high = 0
player_guess = 0
guess_remain = 0
guessTaken = 0
game_choice = 0
secret_number = 0

# define event handlers for control panel
def init():
    global guessTaken, player_guess, low, high, secret_number
    low = 0
    high = 0
    player_guess = 0
    guess_remain = 0
    guessTaken = 0
    game_choice = 0
    

def range100():
    # button that changes range to range [0,100) and restarts
    global low, high, guess_remain, game_choice, secret_number
    game_choice = 100
    low = 0
    high = 100
    secret_number = random.randrange(low, high)
    
    guess_remain = float(math.ceil(math.log(high, 2)))
    print "New game. Range is from ", low, " to ", high
    print 'Number of remaing guesses is ', guess_remain
    print
    
    init()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global low, high, guess_remain, game_choice, secret_number
    game_choice = 1000
    low = 0
    high = 1000
    secret_number = random.randrange(low, high)
    
    guess_remain = float(math.ceil(math.log(high, 2)))
    print "New game. Range is from ", low, " to ", high
    print 'Number of remaing guesses is ', guess_remain
    print
    init()
        
def  loose():
    global secret_number, game_choice
    print "You ran out of guesses. The number was ", secret_number
    print
    if game_choice == 100:
        range100()
    else:
        range1000()
    
    
def get_input(guess):
    # main game logic goes here	
    global guessTaken, low, high, secret_number, game_choice, guess_remain 
           
    player_guess = int(guess)
    if (guess_remain >= 1):
        guess_remain -= 1
        if player_guess < secret_number:
            print('Higher!!')
            print 'Number of remaing guesses is ', guess_remain
            print
            low = player_guess
        
         
        elif player_guess > secret_number:
            print('Lower!!')
            print 'Number of remaing guesses is ', guess_remain
            print
            high = player_guess
        
        
        elif player_guess == secret_number:
            print('Correct!! ')
            print
            if game_choice == 100:
                range100()
            else:
                range1000()
    else:
        loose()
        
# create frame
f = simplegui.create_frame("Guessing Game",300,300)

# register event handlers for control elements
f.add_button("range 0 - 100", range100, 200)
f.add_button("range 0 - 1000", range1000, 200)
f.add_input("Enter a Guess:", get_input, 200)
#init()

# start frame
f.start()

# always remember to check your completed program against the grading rubric
