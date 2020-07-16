
import random
import time
import sys

print("\nLet's play TIC-TAC-TOE! \(ᵔᵕᵔ)/")

available_slots = []

board = [[' ', '|', ' ', '|', ' '],
         ['-', ' ', '-', ' ', '-'],
         [' ', '|', ' ', '|', ' '],
         ['-', ' ', '-', ' ', '-'],
         [' ', '|', ' ', '|', ' ']]

def player_input(row = '', column = ''):
    print()
    for row in board:
        print(str(''.join(row)))

    while True:
        print("\n" + "Choose a row: enter a number between 1 and 3.")
        row = input()

        while row not in ['1', '2', '3']:
            print("Wrong input, try again! Enter a number between 1 and 3.")
            row = input()
        row = (int(row) - 1) * 2

        print("\n" + "Choose a column: enter a number between 1 and 3.")
        column = input()

        while column not in ['1', '2', '3']:
            print("Wrong input, try again! Enter a number between 1 and 3.")
            column = input()
        column = (int(column) - 1) * 2

        if board[row][column] != ' ':
            print("Slot is already taken. Try again!")
        else:
            board[row][column] = 'x'
            print()
            for row in board:
                print(str(''.join(row)))
            break

def check_player_victory():
    # Check if a horizontal line is complete
    while True:
        if board[0][0] == 'x' and board [0][2] == 'x' and board[0][4] == 'x':
            break
        if board[2][0] == 'x' and board [2][2] == 'x' and board[2][4] == 'x':
            break
        if board[4][0] == 'x' and board [4][2] == 'x' and board[4][4] == 'x':
            break

        # Check if a vertical line is complete
        if board[0][0] == 'x' and board [2][0] == 'x' and board[4][0] == 'x':
            break
        if board[0][2] == 'x' and board [2][2] == 'x' and board[4][2] == 'x':
            break
        if board[0][4] == 'x' and board [2][4] == 'x' and board[4][4] == 'x':
            break

        # Check if a diagonal is complete
        if board[0][0] == 'x' and board [2][2] == 'x' and board[4][4] == 'x':
            break
        if board[0][4] == 'x' and board [2][2] == 'x' and board[4][0] == 'x':
            board[4][0] = 'x'
            break
        return False

def complete_line():
    # Complete a horizontal line if missing only one o
    while True:
        if board[0][0] == 'o' and board [0][2] == 'o' and board[0][4] == ' ':
            board[0][4] = 'o'
            break
        if board[0][0] == 'o' and board [0][4] == 'o' and board[0][2] == ' ':
            board[0][2] = 'o'
            break
        if board[0][2] == 'o' and board [0][4] == 'o' and board[0][0] == ' ':
            board[0][0] = 'o'
            break

        if board[2][0] == 'o' and board [2][2] == 'o' and board[2][4] == ' ':
            board[2][4] = 'o'
            break
        if board[2][0] == 'o' and board [2][4] == 'o' and board[2][2] == ' ':
            board[2][2] = 'o'
            break
        if board[2][2] == 'o' and board [2][4] == 'o' and board[2][0] == ' ':
            board[2][0] = 'o'
            break

        if board[4][0] == 'o' and board [4][2] == 'o' and board[4][4] == ' ':
            board[4][4] = 'o'
            break
        if board[4][0] == 'o' and board [4][4] == 'o' and board[4][2] == ' ':
            board[4][2] = 'o'
            break
        if board[4][2] == 'o' and board [4][4] == 'o' and board[4][0] == ' ':
            board[4][0] = 'o'
            break

        # Complete a vertical line if missing only one o
        if board[0][0] == 'o' and board [2][0] == 'o' and board[4][0] == ' ':
            board[4][0] = 'o'
            break
        if board[0][0] == 'o' and board [4][0] == 'o' and board[2][0] == ' ':
            board[2][0] = 'o'
            break
        if board[2][0] == 'o' and board [4][0] == 'o' and board[0][0] == ' ':
            board[0][0] = 'o'
            break

        if board[0][2] == 'o' and board [2][2] == 'o' and board[4][2] == ' ':
            board[4][2] = 'o'
            break
        if board[0][2] == 'o' and board [4][2] == 'o' and board[2][2] == ' ':
            board[2][2] = 'o'
            break
        if board[2][2] == 'o' and board [4][2] == 'o' and board[0][2] == ' ':
            board[0][2] = 'o'
            break

        if board[0][4] == 'o' and board [2][4] == 'o' and board[4][4] == ' ':
            board[4][4] = 'o'
            break
        if board[0][4] == 'o' and board [4][4] == 'o' and board[2][4] == ' ':
            board[2][4] = 'o'
            break
        if board[2][4] == 'o' and board [4][4] == 'o' and board[0][4] == ' ':
            board[0][4] = 'o'
            break

        # Complete a diagonal if missing only one o

        if board[0][0] == 'o' and board [2][2] == 'o' and board[4][4] == ' ':
            board[4][4] = 'o'
            break
        if board[0][4] == 'o' and board [2][2] == 'o' and board[4][0] == ' ':
            board[4][0] = 'o'
            break

        if board[0][0] == 'o' and board [4][4] == 'o' and board[2][2] == ' ':
            board[2][2] = 'o'
            break
        if board[0][4] == 'o' and board [4][0] == 'o' and board[2][2] == ' ':
            board[2][2] = 'o'
            break

        if board[2][2] == 'o' and board [4][4] == 'o' and board[0][0] == ' ':
            board[0][0] = 'o'
            break
        if board[2][2] == 'o' and board [4][0] == 'o' and board[0][4] == ' ':
            board[0][4] = 'o'
            break
        return False

def block_line():
    while True:
        # Block a horizontal line if only missing one x
        if board[0][0] == 'x' and board [0][2] == 'x' and board[0][4] == ' ':
            board[0][4] = 'o'
            break
        if board[0][0] == 'x' and board [0][4] == 'x' and board[0][2] == ' ':
            board[0][2] = 'o'
            break
        if board[0][2] == 'x' and board [0][4] == 'x' and board[0][0] == ' ':
            board[0][0] = 'o'
            break

        if board[2][0] == 'x' and board [2][2] == 'x' and board[2][4] == ' ':
            board[2][4] = 'o'
            break
        if board[2][0] == 'x' and board [2][4] == 'x' and board[2][2] == ' ':
            board[2][2] = 'o'
            break
        if board[2][2] == 'x' and board [2][4] == 'x' and board[2][0] == ' ':
            board[2][0] = 'o'
            break

        if board[4][0] == 'x' and board [4][2] == 'x' and board[4][4] == ' ':
            board[4][4] = 'o'
            break
        if board[4][0] == 'x' and board [4][4] == 'x' and board[4][2] == ' ':
            board[4][2] = 'o'
            break
        if board[4][2] == 'x' and board [4][4] == 'x' and board[4][0] == ' ':
            board[4][0] = 'o'
            break

        # Block a vertical line if only missing one x
        if board[0][0] == 'x' and board [2][0] == 'x' and board[4][0] == ' ':
            board[4][0] = 'o'
            break
        if board[0][0] == 'x' and board [4][0] == 'x' and board[2][0] == ' ':
            board[2][0] = 'o'
            break
        if board[2][0] == 'x' and board [4][0] == 'x' and board[0][0] == ' ':
            board[0][0] = 'o'
            break

        if board[0][2] == 'x' and board [2][2] == 'x' and board[4][2] == ' ':
            board[4][2] = 'o'
            break
        if board[0][2] == 'x' and board [4][2] == 'x' and board[2][2] == ' ':
            board[2][2] = 'o'
            break
        if board[2][2] == 'x' and board [4][2] == 'x' and board[0][2] == ' ':
            board[0][2] = 'o'
            break

        if board[0][4] == 'x' and board [2][4] == 'x' and board[4][4] == ' ':
            board[4][4] = 'o'
            break
        if board[0][4] == 'x' and board [4][4] == 'x' and board[2][4] == ' ':
            board[2][4] = 'o'
            break
        if board[2][4] == 'x' and board [4][4] == 'x' and board[0][4] == ' ':
            board[0][4] = 'o'
            break

        # Block a diagonal if only missing one x

        if board[0][0] == 'x' and board [2][2] == 'x' and board[4][4] == ' ':
            board[4][4] = 'o'
            break
        if board[0][4] == 'x' and board [2][2] == 'x' and board[4][0] == ' ':
            board[4][0] = 'o'
            break

        if board[0][0] == 'x' and board [4][4] == 'x' and board[2][2] == ' ':
            board[2][2] = 'o'
            break
        if board[0][4] == 'x' and board [4][0] == 'x' and board[2][2] == ' ':
            board[2][2] = 'o'
            break

        if board[2][2] == 'x' and board [4][4] == 'x' and board[0][0] == ' ':
            board[0][0] = 'o'
            break
        if board[2][2] == 'x' and board [4][0] == 'x' and board[0][4] == ' ':
            board[0][4] = 'o'
            break
        return False

def update_available_slots():
    available_slots.clear()
    for index_row, row in enumerate(board):
        for index_x, x in enumerate(row):
            if index_row in [0, 2, 4]:
                if x == ' ':
                    available_slots.append([index_row, index_x])
    return(available_slots)

def pick_random_slot():
    random_available_slot = random.sample(available_slots, 1)[0]
    board[int(random_available_slot[0])][int(random_available_slot[1])] = 'o'

def play_again():
    print("Wanna play again? (y/n)")
    answer = input() # to complete
    if answer != 'y':
        sys.exit()
    else:
        board.clear()
        board.extend(([' ', '|', ' ', '|', ' '],
                      ['-', ' ', '-', ' ', '-'],
                      [' ', '|', ' ', '|', ' '],
                      ['-', ' ', '-', ' ', '-'],
                      [' ', '|', ' ', '|', ' ']))
        main()

def main():
    while True:
        if update_available_slots() == []:
            print("\nOh, it's a draw. ¯\_(ツ)_/¯ ")
            play_again()

        player_input()

        if update_available_slots() == []:
            print("\nOh, it's a draw. ¯\_(ツ)_/¯ ")
            play_again()

        # Check if player has won:
        if check_player_victory() != False:
            print("\nCongrats, you won! (҂◡_◡)")
            play_again()

        print("\nOk, my turn. Mmmh... (ఠ_ఠ)")
        time.sleep(1)
        print("Here! (°‿‿°) \n")

        # If a player's line can be blocked, block it:
        if complete_line() != False:
            for row in board:
                print(str(''.join(row)))
            print("\nYay, I won! ᕙ(⇀‸↼‶)ᕗ")
            play_again()

        # If no player line can be blocked, fill a random available slots:
        if block_line() == False:
            pick_random_slot()

main()

