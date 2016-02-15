import random
import math
import sys

def draw_board(board):
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])



def player_select(player,computer):
    player = input("Please choose to be 'X' or 'O':")
    if(player == 'X'):
        computer = 'O'
        return(player, computer)
    elif(player == 'O'):
        computer = 'X'
        return(player, computer)
    else:
        print("Invalid character entered")
        return player_select(player,computer)

def player_choice(player,computer,board,run_game):
    draw_board(board)
    number = input("Player choose a number from 1-9:")
    if(number == '1' and board[0]== ' '):
        board[0] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '2' and board[1]== ' '):
        board[1] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '3' and board[2]== ' '):
        board[2] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '4' and board[3]== ' '):
        board[3] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '5' and board[4]== ' '):
        board[4] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '6' and board[5]== ' '):
        board[5] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '7' and board[6]== ' '):
        board[6] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '8' and board[7]== ' '):
        board[7] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    elif(number == '9' and board[8]== ' '):
        board[8] = player
        winner(run_game,player,computer,board)
        return computer_choice(computer,player,board,run_game)
    else:
        print("Invalid character entered")
        return player_choice(player,computer,board,run_game)

def computer_choice(computer,player,board,run_game):
    draw_board(board)
    number = input("Computer choose a number from 1-9:")
    if(number == '1' and board[0]== ' '):
        board[0] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '2' and board[1]== ' '):
        board[1] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '3' and board[2]== ' '):
        board[2] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '4' and board[3]== ' '):
        board[3] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '5' and board[4]== ' '):
        board[4] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '6' and board[5]== ' '):
        board[5] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '7' and board[6]== ' '):
        board[6] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '8' and board[7]== ' '):
        board[7] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    elif(number == '9' and board[8]== ' '):
        board[8] = computer
        winner(run_game,player,computer,board)
        return player_choice(player,computer,board,run_game)
    else:
        print("Invalid character entered")
        return computer_choice(computer,player,board,run_game)

def quit_retry():
    response = input("\nPlay again?, enter 'y', or quit, enter 'n': ")
    if(response == 'y'):
        main()
    elif(response == 'n'):
        sys.exit()
    else:
        print("Invalid character entered")
        return quit_retry()
    

def winner(run_game,player,computer,board):
    if(board[0] == player and board[1] == player and board[2] == player or
       board[0] == player and board[3] == player and board[6] == player or
       board[0] == player and board[4] == player and board[8] == player or
       board[1] == player and board[4] == player and board[7] == player or
       board[2] == player and board[5] == player and board[8] == player or
       board[3] == player and board[4] == player and board[5] == player or
       board[6] == player and board[7] == player and board[8] == player or
       board[2] == player and board[4] == player and board[6] == player):
        print("\nPlayer Wins!!")
        run_game = False
        draw_board(board)
        return quit_retry()
    
    elif(board[0] == computer and board[1] == computer and board[2] == computer or
       board[0] == computer and board[3] == computer and board[6] == computer or
       board[0] == computer and board[4] == computer and board[8] == computer or
       board[1] == computer and board[4] == computer and board[7] == computer or
       board[2] == computer and board[5] == computer and board[8] == computer or
       board[3] == computer and board[4] == computer and board[5] == computer or
       board[6] == computer and board[7] == computer and board[8] == computer or
       board[2] == computer and board[4] == computer and board[6] == computer):
        print("\nComputer Wins")
        draw_board(board)
        run_game = False
        return quit_retry()
    
    elif(board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and
         board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and
         board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
        print("\nTie!!")
        draw_board(board)
        run_game = False
        return quit_retry()
       
def main():
    
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = ''
    computer = ''
    player, computer = player_select(player,computer)
    run_game = True

    print("\n\nPlayer is %s and computer is %s" % (player,computer))

    while(run_game == True):
        player_f_move = random.randint(1,9)
        computer_f_move = random.randint(1,9)
        
        if(player_f_move > computer_f_move):
            player_choice(player,computer,board,run_game)
            
        elif(computer_f_move > player_f_move):
            computer_choice(computer,player,board,run_game)

        elif(run_game == False):
            quit_retry()
            
        
    

main()
