from game import ChoiceDoorContest
import numpy as np


class AutoCalculator:

    def __init__(self, number_of_doors, trial_number, change_ratio):
        self.number_of_doors = number_of_doors
        self.trial_number = trial_number
        self.change_choice = change_ratio
        self.win_number = 0
        self.lose_number = 0
        self.number_of_change_door = 0

    def loop(self):
        for i in range(self.trial_number):
            game = ChoiceDoorContest(self.number_of_doors)
            chg = np.random.random() < self.change_choice
            if chg:
                self.number_of_change_door += 1
            if game.game_auto(np.random.randint(0, self.number_of_doors), chg):
                self.win_number += 1
            else:
                self.lose_number += 1
        print("Number of trial: ", self.trial_number)
        print("Number of doors: ", self.number_of_doors)
        print("Number of change: ", self.number_of_change_door)
        print("-------------------------")
        print("Win ratio: ", self.win_number / self.trial_number)
        print("Lose ratio: ", self.lose_number / self.trial_number)

if __name__ == "__main__":
    auto = AutoCalculator(100, 100000, 1.0)
    auto.loop()