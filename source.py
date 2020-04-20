import random
import os

def clear():
    os.system( 'cls' )

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    


def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('\nPlayer1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):

    board[position] = marker


def win_check(board,mark):

    #WIN TIC TAC TOE?

    return ((board[7] == board[8] == board[9] == mark) or  #across the top
            (board[4] == board[5] == board[6] == mark) or  #across the middle
            (board[1] == board[2] == board[3] == mark) or  #across the bottom
            (board[7] == board[4] == board[1] == mark) or  #down the left side
            (board[8] == board[5] == board[2] == mark) or  #down the middle
            (board[9] == board[6] == board[3] == mark) or  #down the right side
            (board[7] == board[5] == board[3] == mark) or  #diagonal
            (board[9] == board[5] == board[1] == mark))    #diagonal




def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'



def space_check(board,position):

    return board[position] == ' '



def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False

    # BOARD IS FULL IF WE RETURN TRUE
    return True



def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position



def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    


clear()
print('\nWelcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker , player2_marker = player_input()

    turn = choose_first()
    print('\n' + turn + ' will go first.')

    play_game = input('\nReady to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    ## GAME PLAY

    while game_on:

        if turn == 'Player 1':
            # Player1's turn.

            # Show the board
            clear()
            display_board(theBoard)
            # Choose a position
            position = player_choice(theBoard)
            # Place the marker on the position
            place_marker(theBoard,player1_marker,position)

            # Check if they won
            if win_check(theBoard,player1_marker):
                clear()
                display_board(theBoard)
                print('\nPlayer 1 has won!\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    clear()
                    display_board(theBoard)
                    print('\nThe game is a draw!\n')
                    break
                else:
                    turn = 'Player 2'
                    clear()


        else:
            # Player2's turn.

            # Show the board
            clear()
            display_board(theBoard)
            # Choose a position
            position = player_choice(theBoard)
            # Place the marker on the position
            place_marker(theBoard,player2_marker,position)

            # Check if they won
            if win_check(theBoard,player2_marker):
                clear()
                display_board(theBoard) 
                print('\nPlayer 2 has won!\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    clear()
                    display_board(theBoard)
                    print('\nThe game is a draw!\n')
                    break
                else:
                    turn = 'Player 1'
                    clear()



    if not replay():
        break
