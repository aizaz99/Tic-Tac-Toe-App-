#----- Global Variables


#game board
board = ["-","-","-","-","-","-","-","-","-"]

#If game is still going
game_still_going = True 

#Who won? or Tie?
winner = None

#Whos turn is iter
current_player = "X"


def display_board():
  print(board[0]+ "|" + board[1]+ "|" + board[2])
  print(board[3]+ "|" + board[4]+ "|" + board[5])
  print(board[6]+ "|" +  board[7]+ "|" + board[8])



def play_game():

  #Display Initial Board
  display_board()

  while game_still_going:

    #handle single turn of arbitary player
   handle_turn(current_player)
  
  #Check if the game is over 
   check_if_game_over()
   #Flip the other player
   flip_player()

  #The game has ended
  if winner == "X" or winner == "O" :
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

#Handle turn of arbitary player
def handle_turn(player):
  position = input(" Choose a position from 1 - 9: ")
  position = int(position) -1 #For Getting -1 cuz array starts from 0
  board[position] = "X"
  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():

#Set up global variable
  global winner 

  #checkrows
  row_winer = check_rows()

  #checkcolumns
  column_winner = check_columns()
  #checkdiagnalos
  diagnal_winner = check_diagnals()
   if row_winner:
     #there was a winner
     winner = row_winer()
    elif: column_winner:
      winner = column_winner()
      #there was a winner
    elif: diagnal_winner:
      winner = diagnal_winner()
      #there was a winner
    else:
      winner = None
  return 

def check_rows():
  
  return
def check_columns():
  return
def check_diagnals():
  return


def check_if_tie():
  return 

def flip_player():
  return 

play_game()









#board
#displayboard
#play game
  #Handle Turn
#check win
  #Checkrows
  #check compile
  #check diagonals 
#checktie
#compile