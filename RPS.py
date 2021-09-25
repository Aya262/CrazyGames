import random
# help class for rock paper scissors game
class Rock_Paper_Scissors:
    # choose system choice randomly
    def rand_fun(self):
        rules = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors'
        }
        number = random.randint(1, 3)
        return rules[str(number)]
    # valid user input value
    def vaild_fun(self):
        rules = {
            'r': 'rock',
            'p': 'paper',
            's': 'scissors'
        }
        print("Enter a Character for your Choice : R for Rock , P for Paper , S for Scissors")
        answer = input().strip().lower()
        while (answer != 'r' and answer != 'p' and answer != 's'):
            try:
                raise ValueError("Please , Enter a Vaild Choice : R for Rock , P for paper , S for Scissors")
            except ValueError as err:
                print("Oh it's wrong {} ".format(err))
                answer = input().strip().lower()
        return rules[answer]
    # compare system choice with user choice
    def result_fun(self,sys, user):
        killers = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        if sys == user:
            return 'Tie'
        elif killers[sys] != user:
            return "User"
        else:
            return "Computer"