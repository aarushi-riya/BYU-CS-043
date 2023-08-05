import random


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                " player 1= " + str(self.player1.name) + " vs " +
                " player 2= " + str(self.player2.name) +
                ">")

    def assignGamePiece(self, game_piece, player):
    # assign the Game piece for opponent player
        if game_piece == 'X'
            opponent.game_piece = 'O'
        else
            opponent.game_piece = 'X'

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return self.player1, self.player2
        else:
            return self.player2, self.player1

    def isWinner(self, gp):
        bo = self.board

        # Given a board and a player's game_peice, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == gp and bo[8] == gp and bo[9] == gp) or  # across the top
                (bo[4] == gp and bo[5] == gp and bo[6] == gp) or  # across the middle
                (bo[1] == gp and bo[2] == gp and bo[3] == gp) or  # across the bottom
                (bo[7] == gp and bo[4] == gp and bo[1] == gp) or  # down the left side
                (bo[8] == gp and bo[5] == gp and bo[2] == gp) or  # down the middle
                (bo[9] == gp and bo[6] == gp and bo[3] == gp) or  # down the right side
                (bo[7] == gp and bo[5] == gp and bo[3] == gp) or  # diagonal
                (bo[9] == gp and bo[5] == gp and bo[1] == gp))  # diagonal

    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)


class Board:
    def __init__(self):
        self.board  = [' '] * 10

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                ">")
    def resetBoard (self):
        self.board = [' '] * 10

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def makeMove(self, game_piece, move):
        self.board[move] = game_piece

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree (self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


class Player:
    def __init__(self, name):
        self.name = name
        self.game_piece = None
        self.wins = 0
        self.losses = 0

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                " Name = " + str(self.name) +
                " Piece = " + str(self.game_piece) +
                " Wins = " + str(self.wins) +
                " Losses = " + str(self.losses) +
                ">")

    def selectGamePiece(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
        self.game_piece = letter

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

















def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])





print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    b = Board()
    name = input("Enter the Player 1 Name:")
    p1 = Player(name)
    name = input("Enter the Player 2 Name:")
    p2 = Player(name)
    g = Game(b, p1, p2)

    playerLetter, computerLetter = inputPlayerLetter()
    player, opponent  = g.whoGoesFirst()
    turn = player.name

    player.selectGamePiece()

    g.assignGamePiece(player.game_piece, opponent)

    print('The ' + player.name + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == player.name:
            # Player's turn.
            b.drawBoard()
            move = g.getPlayerMove()
            b.makeMove(player.game_piece, move)

            if g.isWinner(player.game_piece):
                b.drawBoard()
                print('Hooray! {} have won the game!', player.name)
                gameIsPlaying = False
            else:
                if b.isBoardFull():
                    b.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = opponent.name

        else:
            # Opponent's turn.
            b.drawBoard()
            move = g.getPlayerMove()
            b.makeMove(player.game_piece, move)
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
