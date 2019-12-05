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

  print(player + "'s turn.")
  position = input(" Choose a position from 1 - 9: ")


  if position not in ["1","2", "3","4","5","6","7","8","9"]:
    position = input(" Invalid,  Choose a position from 1 - 9: ")
    
  position = int(position) -1 #For Getting -1 cuz array starts from 0
  board[position] = player
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
  if row_winer:
     #there was a winner
     winner = row_winer
  elif column_winner:
      winner = column_winner
      #there was a winner
  elif diagnal_winner:
      winner = diagnal_winner
      #there was a winner
  else:
      winner = None
  return 

def check_rows():
  #Set up global Variables
  global game_still_going

  #check if rows have same value but not dash
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
   
   #if any row has flag return win
  if row1 or row2 or row3:
     game_still_going = False
  #Return winner (X or O )
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]

  return
def check_columns():

#Set up global Variables
  global game_still_going

  #check if rows have same value but not dash
  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board[7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"
   
   #if any row has flag return win
  if col1 or col2 or col3:
     game_still_going = False
  #Return winner (X or O )
  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]



  return
def check_diagnals():

#Set up global Variables
  global game_still_going

  #check if rows have same value but not dash
  diag1 = board[0] == board[4] == board[8] != "-"
  diag2 = board[6] == board[4] == board[2] != "-"
 
   #if any row has flag return win
  if diag1 or diag2:
     game_still_going = False
  #Return winner (X or O )
  if diag1:
    return board[0]
  elif diag2 :
    return board[6]
  



  return


def check_if_tie():
  global game_still_going

  if "-" not in board:
    game_still_going = False
  return 

def flip_player():
  global current_player

  if current_player == "X":
        current_player = "O"
  elif current_player == "O":
    current_player = "X"

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