#rock paper scissor game
import random
user_point = 0
computer_point = 0
value = ["rock","paper","scissor"]
name = input("Enter your name::")
print("       Hey ! ",name)
print("     Hurrah! Let's start the game")
print(" *********************************************")
computer_guess = random.choice(["rock","paper","scissor"])
print(value)
def main():
   while True:
       user_enter = input("Enter your value::")
       if user_enter in value:
          if user_enter == "rock"  and computer_guess == "paper":
            print("you got a point")
            user_point += 1
          elif user_enter == "scissor"  and computer_guess == "paper":
            print("You got a point")
            user_point += 1
          elif user_enter == "rock"   and computer_guess == "scissor":
            print("You got a point")
            user_point += 1
          else:
            print("You missed it")
            computer_point += 1
       else:
            print("Enter the right value from 'rock','scissor' or 'paper'.")
            next =input("Do you want to play another game ::")
            if next == "yes":
             continue
            else:
                print("Game over")
                print("Thank you for your game play")
                print("Your score is " +str(user_point) + ".")
                print("Computer score is " +str(computer_point) + ".")
                print("come again !")
                exit
main()