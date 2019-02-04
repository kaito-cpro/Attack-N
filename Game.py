from common import *
from Board import Board
from Display import Display
from VirtualPlayer import VirtualPlayer

class Game:
    ''' ゲームの実装クラス '''
    def __init__(self, graphic=True):
        self.board = Board()
        self.display = Display(graphic=graphic)
        self.player = VirtualPlayer()

    def play(self):
        ''' ゲームを 1 回行う '''
        self.refresh()
        while True:
            self.show_board()
            self.put()
            if self.ended():
                self.show_result()
                break
            self.switch()

    def refresh(self):
        '''' 初期化 '''
        self.board.refresh()

    def put(self):
        color = self.player.get_color()
        x = self.player.select(self.board)
        self.board.put(x, color)

    def ended(self):
        ''' ゲームが終了したかどうかの判定 '''
        winner = self.get_winner()
        return (self.full() or winner==BLACK or winner==WHITE)

    def show_board(self):
        ''' 盤面の表示 '''
        self.display.show(self.board)

    def show_result(self):
        ''' 終了処理 '''
        self.display.show(self.board)
        self.display.result(self.get_winner())

    def get_winner(self):
        ''' 勝者の color を返す '''
        for x in range(WIDTH):
            for y in range(HEIGHT):
                pos = Position(x, y)
                if self.board.bingo_at(pos):
                    return self.board.get_color(pos)
        return None

    def full(self):
        return self.board.spaces() == []

    def switch(self):
        ''' 手番を入れ替える '''
        self.player.switch()

Game().play()
