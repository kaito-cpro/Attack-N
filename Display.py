from common import *

class Display:
    ''' 表示を担うクラス '''

    TURN = {BLACK: '先攻',  \
            WHITE: '後攻'}
    STONE = {BLACK: '■',    \
             WHITE: '□'}

    def __init__(self, graphic=True):
        ''' ゲームの進行を表示しない場合は graphic=False にする '''
        self.graphic = graphic

    def show(self, board):
        ''' 盤面の表示 '''
        if self.graphic:
            board.show()

    def result(self, winner):
        ''' ゲームの結果を表示 '''
        if self.graphic:
            if winner == None:
                print('Draw')
            else:
                print('Winner: '+self.TURN[winner])
