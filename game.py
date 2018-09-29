#!/usr/bin/env python3

board = {
    1: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
    2: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
    3: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
    4: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
    5: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
    6: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
    7: {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e', 6: 'e'},
}

black = '\x1b[30m'
red = '\x1b[31m'
blue = '\x1b[34m'
clear = '\x1b[0;0m'

def player_change(player):
    if player == 'r':
        return 'b'
    else:
        return 'r'
def print_board(board):
    for row in range(6, 0, -1):
        for column in range(1, 8):
            if board[column][row] == 'e':
                print(f'{black}O {clear}', end='')
            if board[column][row] == 'r':
                print(f'{red}O {clear}', end='')
            if board[column][row] == 'b':
                print(f'{blue}O {clear}', end='')
        print()
    print('1 2 3 4 5 6 7')

def determine_win(board, last_move): #examines the row, column, and diagonals of the last move played on the board to detect a win
    column = list(board[last_move[0]].values())
    row = [board[x][last_move[1]] for x in range(1, 8)]
    diag1 = []
    x = last_move[0]
    y = last_move[1]
    while y > 1 and x < 7:
        y -= 1
        x += 1
    while y < 7 and x > 0:
        diag1.append(board[x][y])
        x -= 1
        y += 1
    diag2 = []
    x = last_move[0]
    y = last_move[1]
    while y > 1 and x > 1:
        y -= 1
        x -= 1
    while y < 7 and x < 8:
        diag2.append(board[x][y])
        x += 1
        y += 1
    win = False
    for x in range(3, len(column)):
        if column[x] == last_move[2] and column[x-1] == last_move[2] and column[x-2] == last_move[2] and column[x-3] == last_move[2]:
            win = last_move[2]
    for x in range(3, len(row)):
        if row[x] == last_move[2] and row[x-1] == last_move[2] and row[x-2] == last_move[2] and row[x-3] == last_move[2]:
            win = last_move[2]
    try:
        for x in range(3, len(row)):
            if diag1[x] == last_move[2] and diag1[x-1] == last_move[2] and diag1[x-2] == last_move[2] and diag1[x-3] == last_move[2]:
                win = last_move[2]
    except IndexError:
        pass
    try:
        for x in range(3, len(row)):
            if diag2[x] == last_move[2] and diag2[x-1] == last_move[2] and diag2[x-2] == last_move[2] and diag2[x-3] == last_move[2]:
                win = last_move[2]
    except IndexError:
        pass

    return win

player = 'r'
win = False
last_move = []
print_board(board)
while win == False:
    if player == 'r':
        column = input(f"{red}Player {player} pick 1-7 > {clear}")
    if player == 'b':
        column = input(f"{blue}Player {player} pick 1-7 > {clear}")
    
    try:
        column = int(column)
        chips = 1
        x = 1
        if 1 <= column <= 7:
            while chips == 1:
                if board[column][x] == 'e':
                    board[column][x] = player
                    chips = 0
                    last_move = [column, x, player]
                    print('\033[2J')
                    print_board(board)
                    if determine_win(board, last_move) != False:
                        if player == 'r':
                            print(f'{red}Player {player} has won the game!{clear}')
                        if player == 'b':
                            print(f'{blue}Player {player} has won the game!{clear}')
                        win = True
                    player = player_change(player)
                if x == 6 and chips == 1:
                    print('please choose another column')
                    chips = 0
                x += 1
    except ValueError:
        pass
