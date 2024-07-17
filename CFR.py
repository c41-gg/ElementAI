import numpy as np

class CFR:
    def __init__(self, actions):
        self.actions = actions
        self.regret_sum = np.zeros(len(actions))
        self.strategy = np.zeros(len(actions))
        self.strategy_sum = np.zeros(len(actions))

    def get_strategy(self):
        normalizing_sum = 0
        for a in range(len(self.actions)):
            self.strategy[a] = self.regret_sum[a] if self.regret_sum[a] > 0 else 0
            normalizing_sum += self.strategy[a]
        for a in range(len(self.actions)):
            if normalizing_sum > 0:
                self.strategy[a] /= normalizing_sum
            else:
                self.strategy[a] = 1.0 / len(self.actions)
            self.strategy_sum[a] += self.strategy[a]
        return self.strategy

    def get_average_strategy(self):
        avg_strategy = np.zeros(len(self.actions))
        normalizing_sum = sum(self.strategy_sum)
        for a in range(len(self.actions)):
            if normalizing_sum > 0:
                avg_strategy[a] = self.strategy_sum[a] / normalizing_sum
            else:
                avg_strategy[a] = 1.0 / len(self.actions)
        return avg_strategy

    def train(self, iterations):
        for _ in range(iterations):
            self.cfr(np.zeros(len(self.actions)), 1, 1)

    def cfr(self, history, p0, p1):
        plays = len(history)
        player = plays % 2
        opponent = 1 - player

        if plays > 1:
            return self.payoff(history)

        strategy = self.get_strategy()
        util = np.zeros(len(self.actions))
        node_util = 0

        for a in range(len(self.actions)):
            next_history = history + [self.actions[a]]
            util[a] = -self.cfr(next_history, p0 * strategy[a], p1) if player == 0 else -self.cfr(next_history, p0, p1 * strategy[a])
            node_util += strategy[a] * util[a]

        for a in range(len(self.actions)):
            regret = util[a] - node_util
            self.regret_sum[a] += (p1 if player == 0 else p0) * regret

        return node_util

    def payoff(self, history):
        # Define the payoff function for your game
        pass
