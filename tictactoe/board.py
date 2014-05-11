'''Defines a Board class to hold the state of a Tic-Tac-Toe game'''


class Board(object):
    '''A 3x3 Tic-Tac-Toe board

    The board is numbered from the top left corner:

    0|1|2
    -+-+-
    3|4|5
    -+-+-
    6|7|8

    The two players ('X', who goes first, and 'O', who goes second) take turns
    placing their mark in an empty square, until someone has three marks in a
    straight line (a win), or there are no more empty squares (a tie).

    For a lot more information, see:
    http://en.wikipedia.org/wiki/Tic-tac-toe
    '''
    # Position states
    BLANK = 0
    MARK_X = X_NEXT = X_WINS = 1
    MARK_O = O_NEXT = O_WINS = 2

    def __init__(self, state=0):
        '''
        Initialize the board

        Keyword arguments:
        state - The state of the board, or 0 (default) for a new game
        '''

        self.board = []
        init_state = state
        for i in range(9):
            mark = state % 3
            self.board.append(mark)
            state /= 3
        x_moves = len([1 for p in self.board if p == self.MARK_X])
        o_moves = len([1 for p in self.board if p == self.MARK_O])
        if state != 0:
            raise ValueError('Bad state {} - too big'.format(init_state))
        if x_moves < o_moves:
            err = 'Bad state {} - too many O moves'.format(init_state)
            raise ValueError(err)
        if x_moves > o_moves + 1:
            err = 'Bad state {} - too many O moves'.format(init_state)
            raise ValueError(err)
        self._has_winner = self.winner() or False

    def __str__(self):
        '''String representation of board'''

        fmt = '''\
{}|{}|{}
-+-+-
{}|{}|{}
-+-+-
{}|{}|{}'''
        s = {
            self.BLANK: ' ',
            self.MARK_X: 'X',
            self.MARK_O: 'O',
        }
        return fmt.format(*[s[x] for x in self.board])

    def state(self):
        '''Return the state number of the board'''
        state = 0
        for p in reversed(self.board):
            state = (state * 3) + p
        return state

    def next_mark(self):
        '''Return which player places the next mark, or None if game over'''
        if self._has_winner:
            return None
        else:
            moves = len([1 for p in self.board if p != 0])
            if moves % 2:
                return self.O_NEXT
            else:
                return self.X_NEXT

    def next_moves(self):
        '''Return valid next moves'''
        if self._has_winner:
            return []
        else:
            return [i for i, p in enumerate(self.board) if p == 0]

    def move(self, pos):
        '''Add the next move to the board'''
        if pos in self.next_moves():
            self.board[pos] = self.next_mark()
        else:
            raise ValueError('{} is an invalid move'.format(pos))

    def winner(self):
        '''Returns the winner, or False if no winner

        Returns 1 (X_WINS) if X is the winner
        Returns 2 (O_WINS) if O is the winner
        '''

        win_sets = (
            (0, 1, 2),  # Row 1
            (3, 4, 5),  # Row 2
            (6, 7, 8),  # Row 3
            (0, 3, 6),  # Column 1
            (1, 4, 7),  # Column 2
            (2, 5, 8),  # Column 3
            (2, 4, 6),  # Rising slash
            (0, 4, 8),  # Falling slash
        )
        winner = None

        for win_set in win_sets:
            items = [self.board[i] for i in win_set]
            if items[0] != self.BLANK and all(x == items[0] for x in items):
                if winner:
                    if items[0] != winner:
                        raise ValueError('Too many winners!')
                else:
                    winner = items[0]
        return winner
