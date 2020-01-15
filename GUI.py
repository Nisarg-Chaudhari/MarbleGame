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
avlb_colour = (84, 240, 219)
white = (255, 255, 255)

win=pygame.display.set_mode((dim,dim))
pygame.display.set_caption("Marble Game")
font1=pygame.font.SysFont("The Times New Roman",50)
font2=pygame.font.SysFont("The Times New Roman",100)

# Game Board
m = 0
e = 1
f = 8
a = 5

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
            elif Gbrd[i][j] == a :
                pygame.draw.circle(win,avlb_colour,(marb_x,marb_y),marble_radius)

def user_input():
    user_x = 0
    user_y = 0
    user_i = 0
    user_j = 0

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            user_x, user_y = pygame.mouse.get_pos()

            for i in range(0,7):
                for j in range(0,7):
                    marb_y = centre + (i-3) * central_distance
                    marb_x = centre + (j-3) * central_distance

                    if math.sqrt((user_x - marb_x)**2 + (user_y - marb_y)**2) <= marble_radius:
                        (user_i,user_j) = (i,j)
    return (user_i,user_j)

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
    global movelst
    if canMove(i,j):
        if (i==0 or i==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                Gbrd[i+2][j] = a
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                Gbrd[i][j+2] = a
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                Gbrd[i][j-2] = a

        elif (j==0 or j==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                Gbrd[i+2][j] = a
            if  Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                Gbrd[i-2][j] = a
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                Gbrd[i][j+2] = a

        elif (i==5 or i==6):
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                Gbrd[i-2][j] = a
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                Gbrd[i][j+2] = a
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                Gbrd[i][j-2] = a

        elif (j==5 or j==6):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                Gbrd[i+2][j] = a
            if  Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                Gbrd[i-2][j] = a
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                Gbrd[i][j-2] = a


        else:
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                Gbrd[i+2][j] = a
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                Gbrd[i][j+2] = a
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                Gbrd[i-2][j] = a
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                Gbrd[i][j-2] = a

def move(i,j):

    if len(movelst) == 1:
        (move_i,move_j) = movelst[0]
    else:
        not_moved = True
        board()
        pygame.display.update()

        while not_moved:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEMOTION:
                user_x, user_y = pygame.mouse.get_pos()
                print(user_x,user_y)
                for mv in movelst:
                    marb_y = centre + (mv[0]-3) * central_distance
                    marb_x = centre + (mv[1]-3) * central_distance
                    if (event.buttons[0] == 1) and (math.sqrt((user_x - marb_x)**2 + (user_y - marb_y)**2) <= marble_radius):
                            (move_i,move_j) = mv
                            not_moved = False



        for mv in movelst:
            Gbrd[mv[0]][mv[1]] = e

    Gbrd[i][j] = e
    Gbrd[move_i][move_j] = m
    if i == move_i:
        if move_j > j:
            Gbrd[i][j+1] = e
        else:
            Gbrd[i][j-1] = e
    elif j == move_j:
        if move_i > i:
            Gbrd[i+1][j] = e
        else:
            Gbrd[i-1][j] = e

def count():
    count=0
    for row in Gbrd:
        for place in row:
            if place == m:
                count+=1
    return count

def status():

    stat="end"
    for i in range(0,7):
        for j in range(0,7):
            if canMove(i,j):
                stat="run"
    if stat=="run":
        return True
    else:
        return False

while status():
    pygame.time.delay(100)
    movelst=[]

    board()
    pygame.display.update()
    (marb_i,marb_j) = user_input()

    if canMove(marb_i,marb_j):
        addmoves(marb_i,marb_j)
        move(marb_i,marb_j)

    event = pygame.event.wait()
    if event.type == pygame.QUIT :
        break

text1 = font1.render("Number of marbles left:-",False,white)
text2 = font2.render(str(count()),False,white)
board()
win.blit(text1,(50,100))
win.blit(text2,(200,200))
pygame.display.update()

event = pygame.event.wait()
if event.type == pygame.QUIT :
    pygame.quit()
