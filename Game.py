import pygame
from pygame.locals import *


pygame.init()


screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe!!!')

game_icon = pygame.image.load('icon1.png')
pygame.display.set_icon(game_icon)

#variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False



#define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (20, 0, 230)
white = (255, 255, 255)
soft_red = (229, 112, 116)

#win text font
font = pygame.font.SysFont('DePixel', 13)

#Play again rect
again_rect = pygame.Rect(screen_width // 2 + 35, screen_height // 2 + 110, 100, 30)



def draw_grid():
    bg = pygame.image.load('bg7.png')
    grid = (68, 45, 48)
    screen.blit(bg)
    for x in range(1,3):
        #horizon and vertical
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)


for x in range(3):
    row = [0] * 3
    markers.append(row)

 
def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            #player 1
            if y == 1:
                #15 px razstoqnie na markera i risuva x
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15),(x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85),(x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            #player 2
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1    
        x_pos += 1    


def check_winner():

    global winner
    global game_over
    y_pos = 0

    for x in markers:
        #proverqva col za pravilna kombinaciq
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #proverqva rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    #proverqva cross top left to bottom right i bottom left to top right
    if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
        

def draw_winner(winner):
    win_text = pygame.image.load('win.png')
    screen.blit(win_text, (0,0))

    again_text = 'Again?'
    again_img = font.render(again_text, True, white)
    pygame.draw.rect(screen, soft_red, again_rect)
    screen.blit(again_img, (screen_width // 2 + 55, screen_height // 2 + 117, 100, 30))


run = True
while run:

    draw_grid()
    draw_markers()

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == 0:

         if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False

            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1
                check_winner()

    


    if game_over == True:
        draw_winner(winner)
        #check for mouseclick to see if player has clicked Play again
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
            clicked = False
        if event.type == pygame.MOUSEBUTTONUP and clicked == False:
            clicked = True
            
            if again_rect.collidepoint(pos):
                #reset veriables
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    markers.append(row)


    pygame.display.update()


pygame.quit()


