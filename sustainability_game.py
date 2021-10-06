import random


class Sustainability:
    def __init__(self, rounds):
        self.dices = []
        self.amount = 6
        self.rounds = rounds
        self.points = 0

    def dice_generator(self):
        for i in range(self.amount):
            dice = random.randint(1, 6)
            self.dices.append(dice)
        return self.dices

    def total_points(self):
        self.points += sum(self.dices)
        return self.points

    def remove_dice(self, index):
        if index > 0:
            self.dices.pop(int(self.dices.index(index)))
            self.amount -= 1
            new_points = self.total_points()*2
            return new_points
        else:
            pass

    def game(self):
        print("Welcome to the sustainability game!\n"
              "Rules:\n"
              "You get 6 dices and will play 10 rounds. \n"
              "After each round the total points of the dices will be counted \n"
              "However you get the opportunity to permentally put away a dice to double your total points that round.\n"
              "The purpose of the game is to get as many points as possible without running out of dices. \n"
              "If you try to put away a dice you dont have, you will have to go again, put you dont use a round \n"
              "Good luck! \n")

        while self.rounds != 0 and self.amount != 0:
            try:
                print(self.dice_generator())
                user_input = int(input("Which dice do you want to put away? If you want to keep all, then write a negative number: "))
                self.remove_dice(user_input)
                print(self.total_points())
                self.dices.clear()
                self.rounds -= 1
            except ValueError:
                print("Its not one of the dices, try again")
                self.dices.clear()

        else:
            if self.amount == 0:
                print("Sorry you don't have any more dices")
            else:
                print(f"Congrats you made it through the game, you ended up with {self.total_points()} points")


if __name__ == '__main__':
    game = Sustainability(10)
    game.game()
