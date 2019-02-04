from Player import Player
from Agent import *

class PlayerFactory:
    ''' プレイヤーの生成クラス '''
    
    def create_player(agent, color):
        player = Player(agent, color)
        return player
