from collections import defaultdict

SPACE = 0
BLACK = 1
WHITE = -1

REVERSE = {BLACK: WHITE, WHITE: BLACK}

HEIGHT = 7
WIDTH = 6
N = 4  # 長さ N のラインを作るゲーム

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_xy(self):
        return self.x, self.y

def in_board(x, y):
    ''' (x, y) が盤面に収まっているかどうかの判定 '''
    if 0<=x<WIDTH and 0<=y<HEIGHT:
        return True
    else:
        return False

def lines():
    ''' 長さ N のラインのリストを生成 '''
    lines = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # (x, y) から 8 方向の長さ N のラインを考える
            if in_board(x+N-1, y):
                lines.append([(x+i, y) for i in range(N)])
            if in_board(x+N-1, y+N-1):
                lines.append([(x+i, y+i) for i in range(N)])
            if in_board(x, y+N-1):
                lines.append([(x, y+i) for i in range(N)])
            if in_board(x-N+1, y+N-1):
                lines.append([(x-i, y+i) for i in range(N)])
            if in_board(x-N+1, y+N-1):
                lines.append([(x-i, y) for i in range(N)])
            if in_board(x-N+1, y-N+1):
                lines.append([(x-i, y-i) for i in range(N)])
            if in_board(x, y-N+1):
                lines.append([(x, y-i) for i in range(N)])
            if in_board(x+N-1, y-N+1):
                lines.append([(x+i, y-i) for i in range(N)])
    return lines

lines_at = defaultdict(list)  # lines_at[x, y] = (board[y][x] を通る長さ N のラインのリスト)
for line in lines():
    for point in line:
        lines_at[point].append(line)
