"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    #count x and y in board
    x_cnt = 0
    o_cnt = 0
    for i in board:
    	for j in i:
    		if j == X:
    			x_cnt += 1
    		elif j == O:
    			o_cnt += 1
    #if x count = 0 and o count =0 then board is in inital state so X's turn

    if x_cnt == 0 and o_cnt == 0:
    	return X
    #otherwise return player with lesser count
    elif x_cnt <= o_cnt:
    	return X
    else:
    	return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    solution = set()
    #looping through tic tac toe board and adding empty cells to actions
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == EMPTY:
    			tup = (i, j)  #tuple with action
    			solution.add(tup)
    return solution

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise exception for invalid action
    if action[0] < 0 or action[0] > 2 or action[0] < 0 or action[0] > 2 or board[action[0]][action[1]] is not EMPTY:
    	raise ValueError('Invalid action')

    #creating deep copy of board
    new_board = [[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]
    for i in range(3):
    	for j in range(3):
    		new_board[i][j] = board[i][j]

    #finding player to perform action on
    p = player(board)

    #performing action on new board
    new_board[action[0]][action[1]] = p

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #checking horizontally
    for i in range(3):
    	if board[i][0] is not EMPTY and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
    		return board[i][0]

    #checking vertically
    for i in range(3):
    	if board[0][i] is not EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
    		return board[0][i]

    #checking diagonally
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    	return board[0][0]
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    	return board[0][2]

    #if nothing matches return None
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #return true if someone has one the game
    if winner(board) is not None:
    	return True

    #check if all cells are filled 
    flag = True
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == EMPTY:
    			return False

    #retunr true as all cells filled
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ans = winner(board)
    if ans == X:
    	return 1
    elif ans == O:
    	return -1
    else:
    	return 0


def maxplayer(board):
	if terminal(board):
		return utility(board)
	ans = -2
	for action in actions(board):
		ans = max(ans, minplayer(result(board, action)))
	return ans

def minplayer(board):
	if terminal(board):
		return utility(board)
	ans = 2
	for action in actions(board):
		ans = min(ans, maxplayer(result(board, action)))
	return ans


def bestmove(board):

	moves = []
	flag = True
	p = player(board)
	if p == O:
		flag = False

	for action in actions(board):
		move = [-1, -1, 2]
		if flag:
			move[2] = -2
		move[0] = action[0]
		move[1] = action[1]
		new_board = result(board, action)

		if p == O:
			res = maxplayer(new_board)    # make more depth tree for X
			move[2] = res

		if p == X:
			res = minplayer(new_board)    # make more depth tree for O
			move[2] = res

		moves.append(move)

    # Find best move
	best_move = [-1, -1]
	if flag:
		best = -2
		for move in moves:
			if move[2] > best:
				best = move[2]
				best_move[0] = move[0]
				best_move[1] = move[1]
	else:
		best = 2
		for move in moves:
			if move[2] < best:
				best = move[2]
				best_move[0] = move[0]
				best_move[1] = move[1]
                
	return best_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    move = bestmove(board)
    ans = (move[0], move[1])
    return ans