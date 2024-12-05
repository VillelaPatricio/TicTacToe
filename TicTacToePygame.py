import pygame

import random

pygame.init()

Coordinates =  {1:(230,30), 2: (430, 30), 3: (630, 30), 4: (230, 230), 5: (430, 230), 6: (630, 230), 7: (230, 430), 8: (430, 430), 9: (630, 430)}
mouse_pos = pygame.mouse.get_pos()
winning_sets = [[1,2,3],[1,4,7],[3,6,9],[7,8,9],[1,5,9],[3,5,7],[2,5,8],[4,5,6]]
registro = [0,0,0,0,0,0,0,0,0,0]
screen = pygame.display.set_mode((800,600))
running = True
computer_turn = False
grid_color = "#612897"

rectangles = []
for key in Coordinates:
    rectangles.append(pygame.Rect((*Coordinates[key],140,140)))
screen.fill("#170055")
#functions area
def cross(coordinatex, coordinatey):
    pygame.draw.line(screen, "#332FD0", (coordinatex + 0, coordinatey + 0),(coordinatex + 140,coordinatey + 140), width = 20)
    pygame.draw.line(screen, "#332FD0", (coordinatex + 140,coordinatey + 0),(coordinatex + 0,coordinatey + 140), width = 20)

def circle(coordinatex, coordinatey):
    pygame.draw.circle(screen, "#E90064", (coordinatex + 70, coordinatey + 70), 80, 15)

def grid():
    pygame.draw.line(screen, grid_color, (400,20), (400,580), width = 10)
    pygame.draw.line(screen, grid_color, (600,20), (600,580), width = 10)
    pygame.draw.line(screen, grid_color, (220,200), (780,200), width = 10)
    pygame.draw.line(screen, grid_color, (220,400), (780,400), width = 10)
    pygame.draw.line(screen, grid_color, (200,0), (200,600), width = 5)

def winner_check():
    global running
    for sets in winning_sets:
        tracker = 0
        for position in sets:
            if registro[position] == "X":
                tracker += 1
            if tracker == 3:
                print("You won!")
                running = False
def append_scores(index,mark):
    global registro
    if registro[index] == 0:
        registro[index] = (str(mark))
        print(registro)

def computer_play():
        global computer_turn
        while computer_turn == True:
            computer_choice = random.randint(1, 9)
            if registro[computer_choice] == 0:
                circle(*Coordinates[computer_choice])
                append_scores(computer_choice, "O")
                print(computer_choice)
                computer_turn = False
                pass

def player_turn():
    global mouse_pos
    global computer_turn
    for casilla in rectangles:
        index = rectangles.index(casilla) +1
        if casilla.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                cross(*Coordinates[index])
                append_scores(index, "X")
                computer_turn = True


#/////////////////////////////
# /////GAME LOOP/////////////
# //////////////////////////                 
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    mouse_pos = pygame.mouse.get_pos()
    
    grid()
    player_turn()
    #computer_play()
    winner_check()
    print(mouse_pos)
    pygame.display.update()
pygame.quit()