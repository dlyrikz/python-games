# implementation of card game - Memory
# Damian Batchelor 

import simplegui
import random

color ="Green"
WIDTH = 800
HEIGHT = 100
cards =[]
exposed = []
card_value = 0

check_cards =["",""]
show = ["","","","","","","","","","","","","","","",""]

grid =[0,0]
counter = 0
val = ["",""]
state = 0

# helper function to initialize globals
def init(): 
    global cards, show, exposed, card_value, check_cards, state, counter
    
    """Set all Exposed cards to False"""
    cards = []
    exposed = [False, False,False, False, False,False,False, False,False,False, False,False, False, False,False, False]
    show = ["","","","","","","","","","","","","","","",""]
    cards = deck(cards)
    card_value = 0
    counter = 0
    check_cards = ["",""]
    
    l.set_text("Moves = "+str(counter))
    state = 0
    
    print check_cards    
def deck(cards):
    for i in range(16):
        if i < 8:
            cards.append(random.randrange(8))
        else:
            #print cards[i - 8]
            cards.append(cards[i - 8])
    random.shuffle(cards)
    return cards 
     
def is_match(card):
    """Returns whether the ball is in the desired range.  """
    
    return card[0] == card[1]

# define event handlers
def mouseclick(pos):
    global state, color, exposed, cards, show, card_value, check_cards, val, counter
    
    # Checks to see if the click was on a Card
    x = pos[0] // 50
    if state == 0:
        #cards = deck(cards) 
        if exposed[x] == False and check_cards[0] == "":
            color = "Green"
            card_value = cards[x]
            val[0] = x   					#position of card
            
            check_cards[0] = card_value 	#add card value to check
            show[x] = card_value   			#add card value to card to expose
            exposed[x] = True				#make exposed visible in the card position
        
            grid[0] = (x * WIDTH // 16) + 10    #grid x
            grid[1] = (HEIGHT // 2 ) + 10		#grid y
            state = 1
           
    elif state == 1:
        if exposed[x] == False and check_cards[1] == "":
            color = "Black"
            card_value = cards[x]
            val[1] = x   					#position of card
            check_cards[1] = card_value 		#add card value to check
            
            show[x] = card_value   				#add card value to card to expose
            exposed[x] = True      				#make exposed visible in the card position
        
            grid[0] = (x * WIDTH // 16) + 10    #grid x
            grid[1] = (HEIGHT // 2 ) + 10		#grid y
        
            state = 2   
         
           
    elif state == 2 and exposed[x] == False:
        #print val[0], val[1]
        if exposed[val[0]] and exposed[val[1]] and check_cards[0] != "" and check_cards[1] != "":
            result = is_match(check_cards)
            if not result:
                #color = "Green"
                show[val[0]] = ""
                show[val[1]] = ""
                exposed[val[0]] = False
                exposed[val[1]] = False
                check_cards[0] = ""	
                check_cards[1] = ""
                check_cards[0] = cards[x]
            else:
                check_cards[0] = ""	
                check_cards[1] = ""
                check_cards[0] = cards[x]
                
        #check_cards[0] = cards[x]
        val[0] = x   						#position of card
        show[x] =  cards[x]  				#add card value to card to expose
        exposed[x] = True      				#make exposed visible in the card position
                        
        grid[0] = (x * WIDTH // 16) + 10    #grid x
        grid[1] = (HEIGHT // 2 ) + 10		#grid y
        counter += 1
        print check_cards
        l.set_text("Moves = "+str(counter))
        state = 1
      
      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        canvas.draw_polygon([(i*WIDTH // 16, 0), (i*WIDTH // 16, HEIGHT), ((i+1) * WIDTH // 16, HEIGHT), ((i+1) * WIDTH // 16, 0)], 2, "black", "Green")
        
    # Draws the player choices using loops
    for c in range(16):
        canvas.draw_text(str(show[c]), [c * WIDTH // 16 + 10, HEIGHT // 2 + 10], 30, "Red")
   
            
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("Green")
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric