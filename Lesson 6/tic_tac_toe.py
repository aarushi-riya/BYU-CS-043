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

    @staticmethod
    def assign_game_piece(game_piece, player):
        # assign the Game piece for opponent player
        if game_piece == 'X':
            player.game_piece = 'O'
        else:
            player.game_piece = 'X'

    def who_goes_first(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return self.player1, self.player2
        else:
            return self.player2, self.player1

    def is_winner(self, gp):
        bo = self.board.board
        # Given a board and a player's game_piece, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter, so we don't have to type as much.
        return ((bo[7] == gp and bo[8] == gp and bo[9] == gp) or  # across the top
                (bo[4] == gp and bo[5] == gp and bo[6] == gp) or  # across the middle
                (bo[1] == gp and bo[2] == gp and bo[3] == gp) or  # across the bottom
                (bo[7] == gp and bo[4] == gp and bo[1] == gp) or  # down the left side
                (bo[8] == gp and bo[5] == gp and bo[2] == gp) or  # down the middle
                (bo[9] == gp and bo[6] == gp and bo[3] == gp) or  # down the right side
                (bo[7] == gp and bo[5] == gp and bo[3] == gp) or  # diagonal
                (bo[9] == gp and bo[5] == gp and bo[1] == gp))  # diagonal

    def get_player_move(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    @staticmethod
    def play_again():
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


class Board:
    def __init__(self):
        self.board = [' '] * 10

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                ">")

    def reset_board(self):
        self.board = [' '] * 10

    def draw_board(self):
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

    def make_move(self, game_piece, move):
        self.board[move] = game_piece

    def get_board_copy(self, dup_board=None):
        # Make a duplicate of the board list and return it the duplicate.
        for i in self.board:
            dup_board.append(i)

        return dup_board

    def is_space_free(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def is_board_full(self):
        # Return True if every space on the board has been taken. Otherwise, return False.
        for i in range(1, 10):
            if self.is_space_free(i):
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

    def select_game_piece(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
        self.game_piece = letter


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    b = Board()
    name = input("Enter the Player 1 Name:")
    p1 = Player(name)
    name = input("Enter the Player 2 Name:")
    p2 = Player(name)
    g = Game(b, p1, p2)

    player, opponent = g.who_goes_first()
    turn = player.name

    print('The ' + player.name + ' will go first.')

    player.select_game_piece()

    g.assign_game_piece(player.game_piece, opponent)

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == player.name:
            # Player's turn.
            b.draw_board()
            move = g.get_player_move()
            b.make_move(player.game_piece, move)

            if g.is_winner(player.game_piece):
                b.draw_board()
                print('Hooray! {} have won the game!', player.name)
                gameIsPlaying = False
            else:
                if b.is_board_full():
                    b.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = opponent.name

        else:
            # Opponent's turn.
            b.draw_board()
            move = g.get_player_move()
            b.make_move(opponent.game_piece, move)

            if g.is_winner(opponent.game_piece):
                b.draw_board()
                print('Hooray! {} have won the game!', opponent.name)
                gameIsPlaying = False
            else:
                if b.is_board_full():
                    b.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = player.name

    if not g.play_again():
        break
