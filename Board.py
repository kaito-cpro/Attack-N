from common import *

class Board:
    ''' 盤面の実装クラス '''
    STONE = {BLACK: '■',    \
             WHITE: '□',    \
             SPACE: '-'}

    def __init__(self):
        self.board = [[SPACE for x in range(WIDTH)] for y in range(HEIGHT)]

    def show(self):
        stone = self.STONE
        for y in range(HEIGHT):
            print('    ', end='')
            for x in range(WIDTH):
                print(self.STONE[self.board[HEIGHT-y-1][x]], end='  ')
            print()
        print()

    def put(self, x, color):
        y = self.lowest_place(x)
        self.board[y][x] = color

    def put_at(self, pos, color):
        ''' pos の位置に color の石を入れる '''
        x, y = pos.to_xy()
        assert y == self.lowest_place(x)
        self.board[y][x] = color

    def remove_at(self, pos, color):
        ''' pos にある石を取り除く '''
        x, y = pos.to_xy()
        self.boad[y][x] = SPACE

    def spaces(self):
        ''' 置ける座標のリストを生成 '''
        spaces = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = Position(x, y)
                if self.available_at(pos):
                    spaces.append(pos)
        return spaces

    def filled(self):
        ''' 置けない座標のリストを生成 '''
        filled = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = Position(x, y)
                if not self.available_at(pos):
                    filled.append(pos)
        return filled

    def available_at(self, pos):
        ''' pos に置けるかどうかの判定 '''
        x, y = pos.to_xy()
        return y == self.lowest_place(x)

    def available(self, x):
        ''' x の列に石を入れることができるかどうかの判定 '''
        return self.lowest_place(x) != None

    def full(self):
        ''' 盤面がすべて埋まっているかどうかの判定 '''
        return self.spaces == []

    def lowest_place(self, x):
        ''' x の列における, 最も低いSPACEがある y 座標 '''
        for y in range(HEIGHT):
            if self.board[y][x] == SPACE:
                return y
        return None

    def bingo_at(self, pos):
        ''' pos を通る長さ N のラインで石が揃っているものがあるかどうかの判定 '''
        x, y = pos.to_xy()
        for line in lines_at[(x, y)]:
            if all(self.board[b][a] == BLACK for a, b in line) or   \
               all(self.board[b][a] == WHITE for a, b in line):
               return True
               break
        return False

    def get_color(self, pos):
        x, y = pos.to_xy()
        return self.board[y][x]

    def refresh(self):
        self.board = [[SPACE for x in range(WIDTH)] for y in range(HEIGHT)]
