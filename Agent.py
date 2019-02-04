from random import choice

class Agent:
    ''' エージェントの基本クラス '''

    def select(self, board):
        pass

    def set_color(self, color):
        self.color = color

class Human(Agent):
    ''' 手動のエージェント '''
    def select(self, board):
        while True:
            x = int(input('>> x = '))
            if board.available(x):
                return x
            else:
                print('>> invalid number!')

class RandomAgent(Agent):
    ''' ランダムに手を選ぶエージェント '''
    def select(self, board):
        pos = choice(board.spaces())
        x, y = pos.to_xy()
        print(f'>> x = {x}')
        return x
        
