"""
Tic Tac Toe - MiniMax Algorithm

Min Player: X
Max Player: O
"""
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """Returns starting state of the board."""
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """Returns name of player whose turn it is."""
    counts = {  X: sum(i.count(X) for i in board),
                O: sum(i.count(O) for i in board)}

    return(min(counts, key=counts.get))


def actions(board):
    """Returns set of all possible actions (i, j) available on the board."""
    actions = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] is EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """Returns the board that results from making move (i, j) on the board."""
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """Returns the winner of the game, if there is one."""
    rows, cols, diags = lines(board)

    for row in rows:
        if winning_line(row):
            return row[0]
    for col in cols:
        if winning_line(col):
            return col[0]
    for diag in diags:
        if winning_line(diag):
            return diag[0]

    return None


def terminal(board):
    """Returns True if game is over, False otherwise."""
    if full(board):
        return True

    rows, cols, diags = lines(board)
    for row in rows:
        if winning_line(row):
            return True
    for col in cols:
        if winning_line(col):
            return True
    for diag in diags:
        if winning_line(diag):
            return True

    return False


def utility(board):
    """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """Returns the optimal action for the current player on the board."""
    if player(board) is X: # (Min)
        return min_(board)[1:]
    return max_(board)[1:] # (Max)


def max_(board):
    maxval = -2
    px = None
    py = None

    if terminal(board):
        result = winner(board)
        if result == X:
            return (-1, 0, 0)
        elif result == O:
            return (1, 0, 0)
        elif result == None:
            return (0, 0, 0)

    """Update: Replace nested loop with action()"""
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] is None:
                board[i][j] = O
                (m, min_i, min_j) = min_(board)
                if m > maxval:
                    maxval = m
                    px = i
                    py = j
                board[i][j] = None

    return(maxval, px, py)


def min_(board):
    minval = 2
    qx = None
    qy = None

    if terminal(board):
        result = winner(board)
        if result == X:
            return (-1, 0, 0)
        elif result == O:
            return (1, 0, 0)
        elif result == None:
            return (0, 0, 0)

    """Update: Replace nested loop with action()"""
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] is None:
                board[i][j] = X
                (m, max_i, max_j) = max_(board)
                if m < minval:
                    minval = m
                    qx = i
                    qy = j
                board[i][j] = None

    return(minval, qx, qy)


def lines(board):
    """Returns all lines in board"""
    rows =  [row for row in board]
    cols =  [[row[0] for row in board],
            [row[1] for row in board],
            [row[2] for row in board]]
    diags =  [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]
    return rows, cols, diags


def winning_line(line):
    """Returns True if line is a winning line"""
    if len(set(line)) == 1 and None not in line:
        return True


def full(board):
    """Returns True if board is a stalemate (full)"""
    if sum([row.count(None) for row in board]) != 0:
        return False
    return True
