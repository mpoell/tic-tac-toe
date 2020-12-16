
import tictactoe as ttt
import itertools

X = "X"
O = "O"
EMPTY = None

# board mid-game
board = ttt.initial_state()
board[0][0] = X
board[0][1] = X
board[0][2] = X
board[1][1] = O
board[2][0] = O
board[2][2] = O
board[2][1] = X

# board empty
board_empty = ttt.initial_state()

# board full
board_full = [  [X, X, X],
                [X, X, X],
                [X, X, X]]



print(ttt.player(board))
print(ttt.player(board))
print(ttt.player(board))



# for line in itertools.zip_longest(rows, cols, diags, fillvalue=[]):
#      winning_line()
