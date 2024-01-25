import random
from tkinter import *

#buttons:
#2d array that represents a grid, initalized to 0 for gameboard. will contain 'Button' type objects
buttons = [[0,0,0], 
           [0,0,0],
           [0,0,0]]


#next_turn : row , column, buttons -> string
#places x/o of the player who clicked on it, and then swaps to the next player's turn
    #row: type -> integer
        # Interp: representing each row on the gameboard from top to bottom
    #column: type -> integer
        # Interp: representing each rown on the gameboard from left to right
def next_turn(row, column): 
    #access to player
    global player

    #check if tile is empty and no one has won
    if buttons[row][column]['text'] == "" and check_winner() is False:

        #if first players turn
        if player == players[0]:

            #place text of player on button they click
            buttons[row][column]['text'] = player

            #if still no winner, swap players and tell next player it is their turn
            if check_winner() is False:
                player = players[1]
                label.config(test=(players[1] + "turn"))

            #if there is a winner tell them they win
            elif check_winner() is True:
                label.config(text=(players[0] + "wins!"))

            #if there is a tie tell them it is a tie
            elif check_winner() == "Tie":
                label.config(text="Tie, well that's boring")

            #if second players turn
        else:

            #place text of player on button they click
            buttons[row][column]['text'] = player

            #if still no winner, swap players and tell next player it is their turn
            if check_winner() is False:
                player = players[0]
                label.config(test=(players[0] + "turn"))

            #if there is a winner tell them they win
            elif check_winner() is True:
                label.config(text=(players[1] + "wins!"))

            #if there is a tie tell them it is a tie
            elif check_winner() == "Tie":
                label.config(text="Tie, well that's boring")

#check_winner
# checks if there is a winner
def check_winner():
    for row in range(3):
        #row win condition
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            #rown
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        #column win condition
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            #turn winning column green
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    #diagonal win condition 1
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        #turn winning diagonal green
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green") 
        return True
    
    #diagonal win condition 2
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "": 
        #turn winning diagonal green
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green") 
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="blue")
        return "Tie"
    
    else:
        return False

#empty_spaces: buttons -> boolean
#check if there are empty spaces left in the game, used in 'check_winner' to see if there are any ties
def empty_spaces(): 

    empty_spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                empty_spaces -= 1

    if empty_spaces == 0:      
          return False

#start a new game instance
def new_game():

    global player

    #reset and randomize players turn
    player = random.choice(players)
    label.config(text=player+"'s turn")

    #reset tile text and colors
    for row in range(3):
        for column in range(3):            
            buttons[row][column].config(text="",bg="#F0F0F0")


#make a window
window = Tk() 
window.title("Tic-Tac-Toe game")

#initlize players
players = ["x", "o"]

#choose a random player to begin the game
player = random.choice(players) 

# a label to indicate whos turn it is
label = Label(text = player + "'s turn", font = ('consolas', 40)) 
label.pack(side="top")

#button to reset the game
reset_button = Button(text="restart", font=('consolas',20), command = new_game)
reset_button.pack(side="top")

#add frame to window
frame = Frame(window)
frame.pack()

#create buttons for grid
for row in range(3):
    for column in range(3):
        #Button is a built in function
        buttons[row][column] = Button(frame, text="", font=('consolas',20), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        #add buttons to frame
        buttons[row][column].grid(row=row, column=column)
        
window.mainloop()