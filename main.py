#-----Global Variables-----
import maya
import pytz
import datetime
today = maya.now()
print(today)
nigeria_timezone = today.datetime(to_timezone='africa/Lagos')
print(nigeria_timezone)
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
#if game is still going on
game_still_going = True


Winner = None 

current_player = "X"

def display_board():
  print(board[0]+'|'+board[1]+'|'+board[2])
  print(board[3]+'|'+board[4]+'|'+board[5])
  print(board[6]+'|'+board[7]+'|'+board[8])
def handle_turn(player):
  position = input('choose a position from 1-9:')
  valid = False
  while not valid:

  
    while position not in['1','2','3','4','5','6','7','8','9']:
      position = input('choose a position from 1-9:')
    
    position = int(position)-1

    if board[position] == "-":
      valid = True
    else:
      print("you cant play there.try again")

  board[position] = player
  display_board()

def check_if_game_over():
  check_if_win()


  check_if_tie()
def check_if_win():
  global Winner
  row_winner = check_row()
  column_winner = check_column()
  diagonal_winner = check_diagonal()
  if row_winner:
    #there was a win
      Winner = row_winner   
  elif column_winner:
    #there was a win
    Winner = column_winner   
  elif diagonal_winner:
    #there was a win
    Winner = diagonal_winner
  else :
    #there is no win
    Winner = None 
  return

  


def check_row():
  global game_still_going
  row_1 = board[0]==board[1]==board[2] !="-"
  row_2 = board[3]==board[4]==board[5] !="-"
  row_3 = board[6]==board[7]==board[8] !="-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_column():
  global game_still_going
  column_1 = board[0]==board[3]==board[6] !="-"
  column_2 = board[1]==board[4]==board[7] !="-"
  column_3 = board[2]==board[5]==board[8] !="-"
  #to stop the while loop if there is a winner 
  if column_1 or column_2 or column_3:
    game_still_going = False
  #return the winner x or o
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2] 
  return

def check_diagonal():
  global game_still_going
  diagonal_1 = board[0]==board[4]==board[8] !="-"
  diagonal_2 = board[2]==board[4]==board[6] !="-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[2]  
  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False 
  return
  

  return
def flip_player():
  global current_player
  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X'
  return  


  return 
 

  


def play_game():
  print("NEW GAME")
  display_board()
  while game_still_going :
    handle_turn(current_player)

    check_if_game_over()

    flip_player()
  if Winner =="X" or Winner=="O":
    print(Winner+" Won")
  elif Winner == None:
    print("Tie.....PLAY AGAIN")
   
   
  
play_game()



