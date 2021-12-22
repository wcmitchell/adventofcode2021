import sys

class bingo_board():
    def __init__(self, entry):
        self.board = [[[a, False] for a in line.split()] for line in entry]

    def call(self, num):
        for row in self.board:
            for val in row:
                if val[0] == num and not val[1]:
                    val[1] = True
                    return

    def check_rows(self):
        for row in self.board:
            win = True
            for _, called in row:
                if not called:
                    win =  False
            if win:
                return True
        return False

    def check_cols(self):
        for col in range(5):
            win = True
            for _, called in [self.board[row][col] for row in range(5)]:
                if not called:
                    win = False
            if win:
                return True
        return False

    def check_wins(self):
        return self.check_cols() or self.check_rows()

    def score(self, call):
        score = 0
        for row in self.board:
            for val, called in row:
                if not called:
                    score+=int(val)
        return score*int(call)


def play(boards, calls):
    for call in calls.split(','):
        winners = []
        if call == '25':
            pass
        for board in boards:
            board.call(call)
            if board.check_wins():
                winner = board
                final_call = call
                if len(boards) > 1:
                    winners.append(winner)
                else:
                    return winner, final_call
        for win in winners:
            boards.remove(win)
    return winner, final_call


def run():
    boards = []
    entry = []
    winner = None
    final_call = None
    with open('./day4input.txt') as f:
        calls = f.readline()
        lines = f.readlines()
        for line in lines[1:]:
            if line == '\n':
                new_board = bingo_board(entry)
                boards.append(new_board)
                entry = []
                continue
            entry.append(line.strip())

    winner, final_call = play(boards, calls)

    print(f'WINNER! {winner.board}')
    print(f'Score: {winner.score(final_call)}')

if __name__ == '__main__':
    run()