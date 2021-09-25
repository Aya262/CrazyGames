import random
import RPS
class CrazyGames:
    ## constructor for the crazy class
    def __init__(self):
        self.rockpaperscissors=RPS.Rock_Paper_Scissors()
        self.name=''
        self.attempts_list=[]
        self.choose()


     ## function that enable user to choose between available games
    def choose(self):
        print("Welcome to Grazy Game Program")
        self.name=input("Enter your name : ")
        while True:
            print("Hi {} ! , Please Enter number of choose you want ".format(self.name))
            print("Press[1] for Mad Story Generator")
            print("Press[2] for Number Guessing ")
            print("Press[3] for binary search algorithm")
            print("Press[4] for Multiplcation Table")
            print("Press[5] for Rock Paper Scissors")
            print("Press[6] for exit the Grazy Game")
            try :
                 number =int(input())
                 if number ==1:
                     self.mad_story_generator()
                 elif number==2:
                     self.number_guessing()
                 elif number==3:
                     self.binary_search_algorithm()
                 elif number==4:
                     self.multiplcation_table()
                 elif number==5:
                     self.rock_paper_scissors()
                 elif number==6:
                     break
                 else :
                     print("Please Enter a valid Choose")
            except ValueError:
                 print("Please Enter a valid Choose")

        print("Thanks {} , See You Again !".format(self.name))


    ##mad story generator game
    def mad_story_generator(self):
        print("Hi {} , Welcome to mad story generator game ^_^".format(self.name))
        loop = 0
        while (loop < 3):
            print("Enter a Noun: ")
            Noun = input()
            print("Enter a verb : ")
            Verb = input()
            print("Enter an objective ")
            objec = input()
            print("Name a place")
            place = input()

            story = "{} will {} the {} in {} in sha Allah ".format(Noun, Verb, objec, place)
            print(story)
            loop += 1

        print("Nice Work {} , See you Again ".format(self.name))
        print("================================================")
    # multiplcation table
    def multiplcation_table(self):
        print("Welcome to Multiplcation Table from 1 to 12")
        print("=============================================")
        for i in range(1, 13):
            for j in range(1, 13):
                print("{} x {} = {}".format(str(i), str(j), i * j), end="     ")
            print("\n")

        print("================================================")
    # number guessing game
    def number_guessing(self):
        print("Welcome Traveller , Welcome to Guessing Game")
        print("Hi {} , Want to Play Guess Game Enter Yes or no ".format(self.name))
        answer = input()
        self.show_score()
        attempt = 0
        number = random.randint(1, 10)
        while answer.lower() == 'yes':
            print("Pick a number between 1 and 10 ")
            try:
                guess = int(input())
                if guess > 10 or guess < 1:
                    raise ValueError("That not a valid number between 1 and 10")
                if number == guess:
                    print("Nice Work , It perfect !")
                    attempt += 1
                    self.attempts_list.append(attempt)
                    print("It tooks you {} attempts".format(attempt))
                    print("Do you want to play again ? Enter yes or no")
                    answer = input()
                    if answer.lower() == 'no':
                        print("Ok, See you again")
                        break
                    else:
                        print("That's Cool , have a good one ")
                        self.show_score()
                        number = random.randint(1, 10)
                        attempt = 0
                elif number > guess:
                    print("No , it greater than that")
                    attempt += 1
                elif number < guess:
                    print("No , it smaller than that")
                    attempt += 1
            except ValueError as err:
                print("That's not a valid number !")
                print("({})".format(err))
        print("Nice Work {} , See you again ".format(self.name))
        print("================================================")
    # help function  for the number guessing game
    def show_score(self):
        if len(self.attempts_list)==0:
            print("There is currently no high score , it's your for the taking ")
        else :
            print("The Current high score is {} ".format(min(self.attempts_list)))
    # recursive function for the binary search algorithm
    def binary_search_recursive(self,list,target):
        index = -1
        s = ''
        min = 0
        max = len(list) - 1
        mid = (min + max) // 2
        if len(list) == 0:
            s = "The number doesn't exist"
        elif list[mid] < target:
            index += mid + 1
            s, index = self.binary_search_recursive(list[mid + 1:], target)
        elif list[mid] > target:
            s, index = self.binary_search_recursive(list[:mid], target)
        else:
            index += mid
            s = "The number {} exist ".format(target)
        return s, index

    # binary search algorithm
    def binary_search_algorithm(self):
        print("Welcome to search Game using recursive binary search algorithm ")
        print("Please Enter the list of number to search in it separated by space")
        items=input().split(' ')
        items=list(map(int,items))
        target=int(input("Enter the Target number : "))
        print(items)
        print(target)
        s,index=self.binary_search_recursive(items,target)
        print("{} at index {}".format(s, index + 1))
        print("Nice Work {} , See you again ".format(self.name))
        print("===============================")
    # rock paper scissors game
    def rock_paper_scissors(self):
        print("Welcome to Rock Paper Scissors Game ")
        User_score = 0
        system_score = 0
        for _ in range(3):
            user = self.rockpaperscissors.vaild_fun()
            system = self.rockpaperscissors.rand_fun()
            print("{} Choice is {}".format(self.name, user))
            print("Computer Choice is {}".format(system))
            winer = self.rockpaperscissors.result_fun(system, user)
            print("Round Winer is {}".format(winer))
            if winer == 'Tie':
                pass
            elif winer == "User":
                User_score += 1
            else:
                system_score += 1
        print("Game Over !")
        print("{} Score is {}".format(self.name, User_score))
        print("Computer Score is {}".format(system_score))
        print("Nice Work {} , See you again ".format(self.name))
        print("==================================================")



# create object from class crazy game
x=CrazyGames()
#x.mad_story_generator()
#x.multiplcation_table()
#x.binary_search_algorithm()
#x.number_guessing()
#x.rock_paper_scissors()
#[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
