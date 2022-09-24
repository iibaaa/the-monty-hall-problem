import numpy as np
import argparse


class ChoiceDoorContest:
    def __init__(self, number_of_doors):
        if number_of_doors < 3:
            raise ValueError("Number of doors must be greater than 2")
        self.doors = self.__create_doors(number_of_doors)
        self.doors_status = np.zeros_like(self.doors)
        self.first_choice = None

    def game_auto(self, selection, change):
        self.first_choice = selection
        self.doors_status[self.first_choice] = 1
        self.__host_open_doors()
        if change:
            new_choice = np.where(self.doors_status == 0)[0][0]
            self.doors_status[new_choice] = 1
            self.doors_status[self.first_choice] = 0
        return self.__check_win()

    def game_manuel_terminal(self):
        self.__print_doors()
        self.first_choice = self.__choose_door()
        self.doors_status[self.first_choice] = 1
        self.__print_doors()
        self.__host_open_doors()
        self.__print_doors()
        print("Do you want to change your choice? (y/n)")
        change_choice = input() == "y"
        if change_choice:
            print("Changing choice...")
            new_choice = np.where(self.doors_status == 0)[0][0]
            print("Your new choice is : ", new_choice)
            self.doors_status[new_choice] = 1
            self.doors_status[self.first_choice] = 0
        self.__print_doors()
        if self.__check_win():
            print("You won!")
            return True
        else:
            print("You lost!")
            return False

    def __check_win(self):
        if self.doors[np.where(self.doors_status == 1)] == 1:
            return True
        else:
            return False

    def __host_open_doors(self):
        # host opens all doors except the one that the player chose and the one with the car
        goats = np.where(self.doors == 0)
        if self.doors[self.first_choice] == 1:
            goats = np.delete(goats, np.random.randint(0, len(goats[0])))
        else:
            pos = np.where(goats[0] == self.first_choice)
            goats = np.delete(goats, pos)
        print(f"Host opens doors: {goats[0] + 1}")
        self.doors_status[goats] = 2

    def __print_doors(self):
        for idx, i in enumerate(self.doors_status):
            if i == 2 and self.doors[idx] == 0:
                print(f" [ G ] ", end=" ")
                continue
            print(f" [ {idx + 1} ] ", end=" ")
        print()
        for idx, i in enumerate(self.doors_status):
            if i == 0:
                print(f" [ X ] ", end=" ")
            elif i == 1:
                print(f" [ S ] ", end=" ")
            elif i == 2:
                print(f" [ O ] ", end=" ")
        print()

    def __choose_door(self):
        choice = input("Choose a door (1-{}): ".format(len(self.doors)))
        return int(choice) - 1

    @staticmethod
    def __create_doors(number_of_doors):
        # zero is the goat, one is the car
        doors = np.zeros(number_of_doors)
        np.random.seed()
        doors[np.random.randint(0, number_of_doors)] = 1
        return doors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number_of_doors", type=int, default=3)
    args = parser.parse_args()
    game = ChoiceDoorContest(args.number_of_doors)
    game.game_manuel_terminal()
