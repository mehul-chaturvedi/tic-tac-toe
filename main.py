board = [0]*9
current_player = None
winner = None
game_still_going = True
player_1_sign = None
player_2_sign = None


# Displays tik-tac-toe board
def display_board():
    for i in range(len(board)):
        if((i+1) % 3 == 0):
            if((i)-3 >= 0):
                print(' | '.join(board[(i+1)-3:i+1]))
            else:
                print(' | '.join(board[:i+1]))


# Starts game logics
def play_game():
    global game_still_going
    while game_still_going:
        display_board()

        player_turn()

        check_if_game_over()
        flip_player()
    if winner:
        print(winner+' won')
        play_again()
    else:
        print('Nobody won')
        play_again()


# Starts a new game, initializes all variable to their default state
def play_new_game():
    global winner, current_player, board, game_still_going, player_1_sign, player_2_sign
    for i in range(9):
        board[i] = '-'
    if player_1_sign == None or player_2_sign == None:
        player_1_sign = input('Player 1 choose your symbol: ')
        player_2_sign = input('Player 2 choose your symbol: ')
    winner = None
    current_player = player_1_sign
    game_still_going = True
    play_game()


# Asks player if they wanna play again
def play_again():
    play_again = input(
        'Wanna play again. Press y for yes, n for no and hit enter: ')
    if play_again == 'y':
        play_new_game()
    else:
        print('Bye Bye.')


# Changes players turn
def flip_player():
    global current_player, player_1_sign, player_2_sign
    if current_player == player_1_sign:
        current_player = player_2_sign
    else:
        current_player = player_1_sign


# Checks if the game is won or tie between players
def check_if_game_over():
    check_if_win()
    check_if_tie()


# Checks if game has been tied
def check_if_tie():
    global game_still_going, winner
    if '-' not in board:
        game_still_going = False
        winner = None
    return


# Asks for position to put player mark
def player_turn():
    position = input('Choose a position to place your mark: ')
    position = int(position)
    if len(position):
        if position < 0 or position > 10:
            print('Please choose position between 1 to 9')
            play_new_game()
            return

    position = position - 1
    if board[position] != '-':
        print('Please choose another position')
        play_game()

    board[position] = current_player
    display_board()


# Checks if any player wins
def check_if_win():
    check_digonal_win(4)
    check_row_win()
    check_col_win()


# Checks if any digonal has all similar player sign
def check_digonal_win(skip):
    global winner, game_still_going
    digonal_1 = board[:9:skip]
    digonal_1_win = all(
        elem == digonal_1[0] and elem != '-' for elem in digonal_1)
    digonal_2 = board[2:8:skip-2]
    digonal_2_win = all(
        elem == digonal_2[0] and elem != '-' for elem in digonal_2)

    if digonal_1_win:
        winner = digonal_1[0]
        game_still_going = False
    elif digonal_2_win:
        winner = digonal_2[2]
        game_still_going = False
    return


# Checks if any row has all similar player sign
def check_row_win():
    global winner, game_still_going
    row_1 = board[:3]
    row_2 = board[3:6]
    row_3 = board[6:9]

    row_1_win = all(ele == row_1[0] and ele != '-' for ele in row_1)
    row_2_win = all(ele == row_2[0] and ele != '-' for ele in row_2)
    row_3_win = all(ele == row_3[0] and ele != '-' for ele in row_3)

    if row_1_win:
        winner = row_1[0]
        game_still_going = False
    elif row_2_win:
        winner = row_2[0]
        game_still_going = False
    elif row_3_win:
        winner = row_3[0]
        game_still_going = False


# Checks if any column has all same player sign
def check_col_win():
    global winner, game_still_going
    col_1 = board[:9:3]
    col_2 = board[1:9:3]
    col_3 = board[2:9:3]

    col_1_win = all(ele == col_1[0] and ele != '-' for ele in col_1)
    col_2_win = all(ele == col_2[0] and ele != '-' for ele in col_2)
    col_3_win = all(ele == col_3[0] and ele != '-' for ele in col_3)

    if col_1_win:
        winner = col_1[0]
        game_still_going = False
    elif col_2_win:
        winner = col_2[0]
        game_still_going = False
    elif col_3_win:
        winner = col_3[0]
        game_still_going = False


play_new_game()
