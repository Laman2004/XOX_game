
Chessboard = [' '] * 10

def showScreen():
    print(' ' + Chessboard[1] + ' ' + '|' + ' ' + Chessboard[2] + ' ' + '|' + ' ' + Chessboard[3])
    print("----------")
    print(' ' + Chessboard[4] + ' ' + '|' + ' ' + Chessboard[5] + ' ' + '|' + ' ' + Chessboard[6])
    print("----------")
    print(' ' + Chessboard[7] + ' ' + '|' + ' ' + Chessboard[8] + ' ' + '|' + ' ' + Chessboard[9])
    print("----------")

def Addstep(letter, cell):
    Chessboard[cell] = letter

def Freecell(cell):
    return Chessboard[cell] == ' '

def Fullcell():
    return Chessboard.count(' ') <= 1

def Winner(letter):
    return ((Chessboard[1] == letter and Chessboard[2] == letter and Chessboard[3] == letter) or
            (Chessboard[4] == letter and Chessboard[5] == letter and Chessboard[6] == letter) or
            (Chessboard[7] == letter and Chessboard[8] == letter and Chessboard[9] == letter) or
            (Chessboard[1] == letter and Chessboard[4] == letter and Chessboard[7] == letter) or
            (Chessboard[2] == letter and Chessboard[5] == letter and Chessboard[8] == letter) or
            (Chessboard[3] == letter and Chessboard[6] == letter and Chessboard[9] == letter) or
            (Chessboard[1] == letter and Chessboard[5] == letter and Chessboard[9] == letter) or
            (Chessboard[3] == letter and Chessboard[5] == letter and Chessboard[7] == letter))

def Playermove():
    cell = int(input("Enter cell between 1 and 9: "))
    if Freecell(cell):
        Addstep('X', cell)
        if Winner('X'):
            showScreen()
            print("Congratulations. You win!")
            return True
        showScreen()
    else:
        print("Cell is full. Try again, please.")
        Playermove()

def Computermove():
    fit_cells = [cell for cell, letter in enumerate(Chessboard) if letter == ' ' and cell != 0]

    for letter in ['O', 'X']:
        for i in fit_cells:
            copy_board = Chessboard[:]
            copy_board[i] = letter
            if Winner(letter):
                return i

    corners = [i for i in fit_cells if i in [1, 3, 7, 9]]

    if corners:
        return random.choice(corners)

    if 5 in fit_cells:
        return 5

    inner = [i for i in fit_cells if i in [2, 4, 6, 8]]

    if inner:
        return random.choice(inner)

def Play():
    print("Welcome to the game")
    showScreen()

    while not Fullcell():
        if Playermove():
            break

        if Fullcell():
            print("Game is a tie!")
            break

        print("--------------------------------------------")

        computer_move = Computermove()
        Addstep('O', computer_move)
        if Winner('O'):
            showScreen()
            print("Computer wins. Try again.")
            break
        showScreen()
        print("--------------------------------------------")

if __name__ == "__main__":
    import random
    Play()

