class Player:
    ''' プレイヤーの実装クラス '''
    def __init__(self, agent, color):
        agent.set_color(color)
        self.agent = agent
        self.color = color

    def select(self, board):
        return self.agent.select(board)
