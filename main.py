
import random

def num_guessing_game(x):
    #print(x)
    give_up = int(input("\nEnter 1 to give up, and 0 to not!: "))
    if give_up == 0:
        user = int(input("\nEnter a number: "))
        if user > x:
            return("Too High")
        elif user < x:
            return("Too Low")
        elif user == x: 
            return("You got it!")
    else:
        return("Give Up?")

def main():
    print("This is the number guessing game!")
    start_now = input("\nLet's start now (press enter): ")

    num_x = random.randint(0, 100)

    val = num_guessing_game(num_x)
    while val != "You got it!":
        if val == "Too High":
            print("\nToo High")
        elif val == "Too Low":
            print("\nToo Low!")
        elif val == "Give Up?":
            print("\nThanks for playing! The answer is ", num_x)
            break

        val = num_guessing_game(num_x)
    if val == "You got it!":
        return("You got it!")

print(main())
