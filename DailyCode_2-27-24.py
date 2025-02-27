import pygame
import math
pygame.init()
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800,800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

# CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
keys = [False, False, False, False, False] #this list holds whether each key has been pressed

# MAP: 2 is brick
map1 = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 3, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2],
    [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
    [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ]

map2 = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ]

map = map1


brick = pygame.image.load("Downloads/easy-top-down-grid-main/easy-top-down-grid-main/brick.png")
stone = pygame.image.load("Downloads/easy-top-down-grid-main/easy-top-down-grid-main/stone.png")
warp = pygame.image.load("Downloads/easy-top-down-grid-main/easy-top-down-grid-main/warp.png")
pot = pygame.image.load("Downloads/easy-top-down-grid-main/easy-top-down-grid-main/pot.png")
pot.set_colorkey((255, 255, 255))
monster = pygame.image.load("Downloads/easy-top-down-grid-main/easy-top-down-grid-main/monster.png")
monster.set_colorkey((255, 255, 255))
Link = pygame.image.load("Downloads/easy-top-down-grid-main/easy-top-down-grid-main/link.png")  # load your spritesheet
Link.set_colorkey((255, 0, 255))  # this makes bright pink (255, 0, 255) transparent (sort of)

# player variables
xpos = 100  # xpos of player
ypos = 700  # ypos of player

monsterx = 520
monstery = 150
monsterTicker = 0
monsterAlive = True

potx = 480
poty = 100

# animation variables variables
frameWidth = 13
frameHeight = 20
RowNum = 0  # for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

while not gameover:
    clock.tick(60)  # FPS

    for event in pygame.event.get():  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        #keyboard input---------------------------
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_a:
                keys[LEFT] = True
            elif event.key == pygame.K_d:
                keys[RIGHT] = True
            elif event.key == pygame.K_w:
                keys[UP] = True
            elif event.key == pygame.K_s:
                keys[DOWN] = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_a:
                keys[LEFT] = False
            elif event.key == pygame.K_d:
                keys[RIGHT] = False
            elif event.key == pygame.K_w:
                keys[UP] = False
            elif event.key == pygame.K_s:
                keys[DOWN] = False




    #MOVEMENT-------------------------------------
    if keys[LEFT] == True:
        vx = -3
        RowNum = 0
        direction = LEFT

    elif keys[RIGHT] == True:
        vx = 3
        RowNum = 1
        direction = RIGHT
    
    elif keys[UP] == True:
        vy = -3
        RowNum = 2
        direction = UP

    elif keys[DOWN] == True:
        vy = 3
        RowNum = 3
        direction = DOWN
        
    else:
        vx = 0
        vy = 0

    #map collision---------------------
    #left collision
    if map[int((ypos) / 40)][int((xpos - 5) / 40)] == 2 :
        xpos+=3
        print("left collision!")
       
    #right collision
    if map[int((ypos) / 40)][int((xpos + 15) / 40)] == 2:
        xpos-=3   
        print("right collision!") 
        
    if map[int((ypos - 5) / 40)][int(xpos / 40)] == 2:
        ypos += 3
        print("up collision!")

    if map[int((ypos + 15) / 40)][int(xpos / 40)] == 2:
        ypos -= 3
        print("down collision!")


    xpos+=vx #update player xpos
    ypos+=vy

    if map[int(ypos / 40)][int(xpos / 40)] == 3:
        if map == map1:
            map = map2
        elif map == map2:
            map = map1

    if ((potx + 60) > (xpos - 5) > (potx)) and ((poty + 60) > (ypos) > (poty)) :
        xpos+=3
    if ((potx + 60) > (xpos - 15) > (potx)) and ((poty + 60) > (ypos) > (poty)) :
        xpos-=3 
            
    if (monsterx < xpos < monsterx + 50) and (monstery + 10 < ypos < monstery + 50):
        gameover = True


    monsterTicker+=1
    if monsterTicker > 400:
        monsterTicker = 0

    if 100 > monsterTicker > 0:
        monstery-=1
    elif 200 > monsterTicker > 100:
        monsterx-=1
    elif 300 > monsterTicker > 200:
        monstery+=1
    elif 400 > monsterTicker > 300:
        monsterx+=1
    # Animation update
    ticker+=1
    if vx != 0: #only animate when moving
        if ticker % 10 == 0:  # only change frames every 10 ticks (make number smaller for faster running animation)
            frameNum += 1
    if frameNum > 7:
        frameNum = 0

    # Render section--------------------------------------------------------
    screen.fill((0, 0, 0))  # wipe screen so it doesn't smear
    # draw map
    for i in range(20):
        for j in range(20):
            if map[i][j] == 2:
                screen.blit(brick, (j * 40, i * 40), (0, 0, 40, 40))
            elif map[i][j] == 3:
                screen.blit(warp, (j * 40, i * 40), (0, 0, 40, 40))

    # draw player
    screen.blit(Link, (xpos, ypos), (frameWidth * frameNum, RowNum * frameHeight, frameWidth, frameHeight))
    screen.blit(monster, (monsterx, monstery), (0, 0, 60, 60))
    screen.blit(pot, (potx, poty), (0, 0, 60, 60))
    pygame.display.flip()  # this actually puts the pixel on the screen

# end game loop
pygame.quit()

