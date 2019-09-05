#Set board list with empty string in the list.
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#Set variable for mark, win, draw, player, and when the game running.
mark = 'x'
win = 1
tie = -1
player = 1
running = 0
game = running

#Display the game introduction.
def opening():
    print('-Tic Tac Toe-')
    print('*First Player - X and Second Player - O*')

#Ask the player to start the game.
def game_start():
    start_game = str.lower(input('Type "s" to start the game: '))

    #If the player input S/s to start the game then play the game or else ask the player again.
    if (start_game == 'S' or start_game == 's'):
        print('Game Start')
        play_game()
    else:
        print('That is not a valid option.')
        game_start()

#Create the game board.
def create_board():
    #https://codereview.stackexchange.com/questions/71521/tic-tac-toe-in-python

    str_board =('''
    | {0} | {1} | {2} |
    -------------
    | {3} | {4} | {5} |
    -------------
    | {6} | {7} | {8} |'''.format(board[0],board[1],board[2],board[3],board[4],
    board[5],board[6],board[7],board[8]))

    #display the board.
    print(str_board)

#Check if the tile is empty or else show the error message that tile is taken and
#ask the player to choose diffent tile.
def check_empty_tile(x):
    if(board[x] == ' '):
        return True
    else:
        print('..............................................')
        print('Tile is taken! Please choose different number.')
        return False

#Winner condition.
#8 condition of horizontal, vertical, and diagonal way of winning.
#if the mark in each board not the same to each other then the game is tie.
#else the board still empty and the game still running.
def winner_state():
    global board
    global game

    if((board[0]==board[1]==board[2] and board[0]!=' ') or
        (board[3]==board[4]==board[5] and board[3]!=' ') or
        (board[6]==board[7]==board[8] and board[6]!=' ') or
        (board[0]==board[3]==board[6] and board[0]!=' ') or
        (board[1]==board[4]==board[7] and board[1]!=' ') or
        (board[2]==board[5]==board[8] and board[2]!=' ') or
        (board[0]==board[4]==board[8] and board[0]!=' ') or
        (board[2]==board[4]==board[6] and board[2]!=' ')):
        game = win
    elif(board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and 
    board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' '):
        game = tie
    else:
        game = running

#Function to play the game.
def play_game():
    global player

    #while game is still running, create the board. 
    while (game == 0):     
        create_board()

        #Mark x for the first player or else mark o for the second player
        if(player % 2 != 0):    
            print('\n Player 1 turn to move.')    
            mark = 'X'    
        else:    
            print('\n Player 2 turn to move.')    
            mark = 'O'
        
        #Ask the player to choose between 0-8.
        move = int(input('Make your move! Choose between numbers [0-8]: '))
        #If player chosen number doesn't have a mark from another player,
        #add the mark and apply the winner_state() function.
        if(check_empty_tile(move)):    
            board[move] = mark    
            player += 1    
            winner_state()    
    
    #Display the winner or if the match tie.
    if (game == tie):    
        print("Game Tie \n")

        #ask the player if the player want to play again.
        play_again()
    elif (game == win):    
        player -= 1

        #First player winning or else second player win the game.   
        if(player % 2 != 0):    
            print('\n Congratulation! Player 1 Won. \n')
            print('Thank you for playing!')
            play_again()    
        else:
            print('\n Congratulation! Player 2 Won. \n')
            print('Thank you for playing!')
            play_again()

#Ask the player if the want to play again.
def play_again():
    print('Do you still want to play? (y/n): ')
    play_more = input()
    if play_more == 'y':
        print('Lets Play again! \n')
        game_start()
    else:
        print('Thank you for playing!')
        
#Call the opening, game_start, and play_game function.
opening()
game_start()
play_game()