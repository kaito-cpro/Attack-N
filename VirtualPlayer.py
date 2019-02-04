from common import *
from PlayerFactory import PlayerFactory
from Agent import *

class VirtualPlayer:

    def __init__(self):
        self.player1 = PlayerFactory.create_player(Human(), BLACK)  # 手動プレイヤ
        self.player2 = PlayerFactory.create_player(RandomAgent(), WHITE)  # ランダムプレイヤー

        self.turn = {self.player1: self.player2,
                     self.player2: self.player1}

        self.player = self.player1

    def switch(self):
        self.player = self.turn[self.player]

    def select(self, board):
        return self.player.select(board)

    def get_color(self):
        return self.player.color
