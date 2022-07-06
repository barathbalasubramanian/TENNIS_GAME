import pygame 
import math
import random
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption(" TENNIS ")
player_img = pygame.image.load("line.png")
ball_img = pygame.image.load("tennis ball.png")
score = 0

# player 1 
x_p1 = 10
y_p1 = 200
p1_change = 0

def player_1 (x,y) :
    screen.blit(player_img , (x,y))
    
# player 2 
x_p2 = 10
y_p2 = 600
p2_change = 0

def player_2 (x,y) :
    screen.blit(player_img , (x,y))
    
# player 3 
x_p3 = 730
y_p3 = 200
p3_change = 0

def player_2 (x,y) :
    screen.blit(player_img , (x,y))
    
# player 4 
x_p4 = 730
y_p4 = 600
p4_change = 0

def player_4 (x,y) :
    screen.blit(player_img , (x,y))   

all_image = [player_img,player_img,player_img,player_img]
x_axis = [x_p1,x_p2,x_p3,x_p4]
y_axis = [y_p1,y_p2,y_p3,y_p4]
changes = [p1_change,p2_change,p3_change,p4_change]

    
# ball 
 
comment = "wait"
ball_x = 400
ball_y = 400
ballchange_x = 0.2
ballchange_y = 0.3
def ball (x,y) :
    global comment 
    comment = "start"
    screen.blit(ball_img,(x,y))

# touching

def istouch(ball_x,ball_y,player_x,player_y) :
    distance = math.sqrt(math.pow(player_x - ball_x,2) + math.pow(player_y - ball_y,2))
    if distance < 20 :
        print(distance)
        return True 
    else :
        return False 
    
exist = True
while exist:
    screen.fill((255,0,0))
    for event in pygame.event.get():
        #exist from screen
        if event.type == pygame.QUIT:
            exist  = False
        # player 1 movement 

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_TAB :
                p1_change = -0.3
            if event.key == pygame.K_CAPSLOCK:
                p1_change = 0.3
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_TAB or event.key == pygame.K_CAPSLOCK :
                p1_change = 0
        
        # player 4 movement 
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                p4_change = -0.3
            if event.key == pygame.K_DOWN :
                p4_change = 0.3
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                p4_change = 0
        
        # player 2 movement
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_s :
                p2_change = -0.3
            if event.key == pygame.K_x :
                p2_change = 0.3
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_s or event.key == pygame.K_x :
                p2_change = 0
            
        # player 3 movement
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_b :
                p3_change = -0.3
            if event.key == pygame.K_SPACE :
                p3_change = 0.3
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_b or event.key == pygame.K_SPACE :
                p3_change = 0 
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_0 :
                comment = "start"
        
    for i in range(4) :
        
        if comment == "start" :
            ball_x += ballchange_x
        # if ball_x >= 730 :
        #     ballchange_x = -0.2
        # if ball_x <= 40 :
        #     ballchange_x = 0.2    
        
            ball_y += ballchange_y
            if ball_y >= 730 :
                ballchange_y = -0.2
            if ball_y <= 40 :
                ballchange_y = 0.2
            
            ball(ball_x,ball_y)
        
            # boundaries for p1        
            
            y_p1 += p1_change     
            if y_p1 >=  330 :
                y_p1 = 330
            if y_p1 <= 10 :
                y_p1 = 10
                
            # boundaries for p2       

            y_p2 += p2_change     
            if y_p2 <=  400 :
                y_p2 = 400
            if y_p2 >= 720 :
                y_p2 = 720
                    
            # boundaries for p4      

            y_p4 += p4_change     
            if y_p4 <= 400 :
                y_p4 = 400
            if y_p4 >= 720 :
                y_p4 = 720
                    
            # boundaries for p3   

            y_p3 += p3_change     
            if y_p3 >=  330 :
                y_p3 = 330
            if y_p3 <= 10 :
                y_p3 = 10
                    
            # is touching 
            
            touch = istouch(ball_x,ball_y,x_axis[i],y_axis[i])
            
            if touch :
                
                if i == 1 :
                    ballchange_x = 0.2
                    score_1 = 1 + score 
                    print (" player 1 :" + str(score_1))
                if i == 2 : 
                    ballchange_x = 0.2
                    score_2 = 1 + score 
                    print (" player 2 :" + str(score_2))
                if i == 3 :
                    ballchange_x = -0.2
                    score_3 = 1 + score 
                    print (" player 3 :" + str(score_3))
                if i == 4 :
                    ballchange_x = -0.2
                    score_4 = 1 + score
                    print (" player 4 :" + str(score_4))   
                ball_x += ballchange_x
            else :
                if ball_x > 800 or  ball_x < 0 :
                    ball_x = 400
                    ball_y = random.randint(200,600)
            
                    
        
        
             
            
        
        
            
    player_1(x_p1,y_p1)
    player_1(x_p2,y_p2)
    player_1(x_p3,y_p3)
    player_1(x_p4,y_p4)
    
    pygame.display.update()