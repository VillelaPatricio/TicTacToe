import random
playername = input("Welcome Player 1 to Tic Tac Toe!! This is my first real trial of code!! ^^ \nPlease type your name to start! ^^\n") 
board_cells = ["_","_","_","_","_","_","_"," "," "," "]
board = "_" + (board_cells[1]) + "_|_" + (board_cells[2]) + "_|_" + (board_cells[3]) + "_ \n" + "_" + (board_cells[4]) + "_|_" + (board_cells[5]) + "_|_" + (board_cells[6]) + "_ \n" + " " + (board_cells[7]) + " | " + (board_cells[8]) + " | " + (board_cells[9])  
playersturn = True
winner = False
tie = False

winning_sets = [[1,2,3],[1,4,7],[3,6,9],[7,8,9],[1,5,9],[3,5,7],[2,5,8],[4,5,6]]

def check_winner():
    global winner
    tracker = 0
    computer_tracker = 0
    for sets in winning_sets:
        #print("Checking on set: ", str(sets))
        for position in sets:
            #print("Checking on position: ", str(position))
            if board_cells[position] == "X":
                #print("Added on: ", str(board_cells[position]))
                tracker += 1
                #print(tracker)
            elif board_cells[position] == "O":
               # print("Computer Added on: ", str(board_cells[position]))
                computer_tracker += 1
                #print(computer_tracker)
                
        if tracker < 3 and computer_tracker < 3:
            tracker = 0
            computer_tracker = 0
            #if board_cells[1:6] != "_" and board_cells[7:9] != " ":
            #if board_cells[1:9] == "X" or board_cells[1:9] == "O":
                #print("It's a tie!. Try again")
        elif tracker == 3:
            #print(sets)
            #print(board_cells)
            print("You won!")
            winner = True
            break
        elif computer_tracker == 3:
            #print(sets)
            #print(board_cells)
            print("Computer won!")
            winner = True
            break

def update_board():
    board = f"{board_cells[1]}_|_{board_cells[2]}_|_{board_cells[3]}_ \n{board_cells[4]}_|_{board_cells[5]}_|_{board_cells[6]}_ \n{board_cells[7]} | {board_cells[8]} | {board_cells[9]} "
    print(board)

def user_input():
    status_turn = True
    global board_cells
    global playersturn
    
    while status_turn == True:
        playing_cell = int(input("~~Please enter a number between 1 to 9 to select a cell\n"))
        if playing_cell in range(1,10):
            if board_cells[playing_cell] == "_" or board_cells[playing_cell] == " ": 
                print("Great Move!")
                board_cells[playing_cell] = "X"
                update_board()
                status_turn = False
            else: 
                print("Sorry, invalid cell")
        else: 
            print("Wrong range!!")

def computer_turn():
    computerturn = True
    while computerturn == True:
        computer_cell = random.randint(1, 9)
        if board_cells[computer_cell] == "_" or board_cells[computer_cell] == " ":
            print("Computer's Choice: " + str(computer_cell))
            board_cells[computer_cell] = "O"
            update_board()
            break
def tie_check():
    global tie
    global winner
    if winner == False:
        if all(i == "X" or i == "O" for i in board_cells[1:10]):
            print("It's a tie!. Try again")
        
        

#Game Sequence    
    
print("Thank you {name}".format(name=playername))
print("This will be the board: " )
print(board)
print("Each cell represent a number from 1 to 9, type the number of cell you want to play at to assign your token to the board")


while winner == False:
    user_input()
    check_winner()
    computer_turn()
    check_winner()
    tie_check()
    print(winner)
#if winner == False and board_cells[1:9] == str:
   # print("It's a tie!. Try again")