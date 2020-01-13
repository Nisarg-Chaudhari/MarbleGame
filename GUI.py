import pygame

pygame.init()

#Diaply Parameters
dim = 500
centre = int(dim/2)

#Board Parameters
board_radius = 230
marble_radius = 20
padding = 15
central_distance = 2 * marble_radius + padding

#Colours
board_colour = (0, 80, 0)
board_border = (0,75,0)
background = (47, 79, 79)
marb_colour = (0, 70, 0)
empty_colour = black = (0,0,0)
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

def board():

    win.fill(background)
    pygame.draw.circle(win,board_colour,(centre,centre),board_radius)
    pygame.draw.circle(win,board_border,(centre,centre),board_radius,3)

    for i in range(0,7):
        for j in range(0,7):
            if Gbrd[i][j] == m :
                marb_y = centre + (i-3) * central_distance
                marb_x = centre + (j-3) * central_distance
                pygame.draw.circle(win,marb_colour,(marb_x,marb_y),marble_radius)
            elif Gbrd[i][j] == e :
                marb_y = centre + (i-3) * central_distance
                marb_x = centre + (j-3) * central_distance
                pygame.draw.circle(win,empty_colour,(marb_x,marb_y),marble_radius)

while True:
    pygame.time.delay(100)
    board()
    pygame.display.update()
