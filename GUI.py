import pygame
import math

pygame.init()

#Diaply Parameters
dim = 500
centre = int(dim/2)

#Board Parameters
board_radius = 230
border_width = 3
marble_radius = 20
padding = 15
central_distance = 2 * marble_radius + padding

#Colours
board_colour = (0, 80, 0)
board_border = (0,75,0)
background = (47, 79, 79)
marb_colour = black = (0, 0, 0)
empty_colour = (0,70,0)
white = (255, 255, 255)
blue = (53, 115, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
yellow = (255, 255, 0)

win=pygame.display.set_mode((dim,dim))
pygame.display.set_caption("Marble Game")

# Game Board
m=0
e=1
f=8

Gbrd = [[f,f,m,m,m,f,f],
        [f,f,m,m,m,f,f],
        [m,m,m,m,m,m,m],
        [m,m,m,e,m,m,m],
        [m,m,m,m,m,m,m],
        [f,f,m,m,m,f,f],
        [f,f,m,m,m,f,f]]
movelst=[]

def board():

    win.fill(background)
    pygame.draw.circle(win,board_colour,(centre,centre),board_radius)
    pygame.draw.circle(win,board_border,(centre,centre),board_radius,border_width)

    for i in range(0,7):
        for j in range(0,7):
            marb_y = centre + (i-3) * central_distance
            marb_x = centre + (j-3) * central_distance
            if Gbrd[i][j] == m :
                pygame.draw.circle(win,marb_colour,(marb_x,marb_y),marble_radius)
            elif Gbrd[i][j] == e :
                pygame.draw.circle(win,empty_colour,(marb_x,marb_y),marble_radius)

def user():
    user_x = 0
    user_y = 0
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            user_x, user_y = pygame.mouse.get_pos()

            for i in range(0,7):
                for j in range(0,7):
                    marb_y = centre + (i-3) * central_distance
                    marb_x = centre + (j-3) * central_distance

                    if math.sqrt((user_x - marb_x)**2 + (user_y - marb_y)**2) <= marble_radius:
                        return (i,j)
def canMove(i,j):

    if Gbrd[i][j]==m:
        if (i==0 or i==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False

        elif (j==0 or j==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            else:
                return False

        elif (i==5 or i==6):
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False

        elif (j==5 or j==6):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False
        else:
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            elif Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False
    else:
        return False

def addmoves(i,j):
    global movelst,poslst
    if canMove(i,j):
        if (i==0 or i==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))

        elif (j==0 or j==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
            if  Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))

        elif (i==5 or i==6):
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))

        elif (j==5 or j==6):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
            if  Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))


        else:
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))



while True:
    pygame.time.delay(100)
    board()
     user()

    pygame.display.update()
