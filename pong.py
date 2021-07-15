# Damian Batchelor

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

paddle1_pos = [0, HEIGHT / 2]
paddle2_pos = [WIDTH, HEIGHT / 2]

paddle1_vel = 0
paddle2_vel = 0

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

vel = [ random.randrange(120, 240) / 45, -random.randrange(60, 180) / 45]

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    
    global ball_pos, ball_vel, vel # these are vectors stored as lists
        
    if (right == True):
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel = [-random.randrange(120, 240) / 45 , -random.randrange(60, 180) / 45]
        ball_vel = [vel[0], vel[1]]
        #print vel
        #print ball_vel
        
    elif (right == False):
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel = [ random.randrange(120, 240) / 45 , - random.randrange(60, 180) / 45]
        ball_vel = [vel[0], vel[1]]
        #print vel
        #print ball_vel
        
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, vel  # these are floats
    global score1, score2  # these are ints
    
    vel = [random.randrange(120, 240) / 45, -random.randrange(60, 180) / 45]
    paddle1_vel = 0
    paddle2_vel = 0
    
    paddle1_pos = [0, HEIGHT / 2]
    paddle2_pos = [WIDTH, HEIGHT / 2]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, vel
 
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    if paddle1_pos[1] <= HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    elif paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
   
        
    if paddle2_pos[1] <= HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
    elif paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
   
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "Blue")
    c.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "Red")
    
    # update ball
    ball_pos[0] += vel[0] 
    ball_pos[1] += vel[1] 
    
    
    # collide and reflect off of left paddle side of canvas
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and ball_pos[1] >= (paddle1_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT):
        vel[0] = - vel[0] 
        #print "Vel [0] PADDLE: ", vel[0]
        ball_vel[0] = vel[0] + vel[0] / 10 
        vel = [ball_vel[0], vel[1]]
       
        
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and (ball_pos[1] < (paddle1_pos[1] - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos[1] + HALF_PAD_HEIGHT)):        
        score2 += 1
        ball_init(True)
        
    # collide and reflect off of right paddle side of canvas    
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS) and ball_pos[1] >= (paddle2_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT):
        vel[0] = - vel[0]
        ball_vel[0] = vel[0] + vel[0] / 10 
        vel = [ball_vel[0], vel[1]]     
        
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS) and (ball_pos[1] < (paddle2_pos[1] - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos[1] + HALF_PAD_HEIGHT)):        
        score1 += 1
        ball_init(False)
           
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    
    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= ((HEIGHT - 1)- BALL_RADIUS):
        vel[1] = - vel[1]
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score1), (WIDTH / 4, HEIGHT / 6), 24, "White")
    c.draw_text(str(score2), (WIDTH / 1.5, HEIGHT / 6), 24, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    acc = 10
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc 
    
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()