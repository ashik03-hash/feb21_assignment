import sys
import random



def play_rps():
       
        playerchoice=input("Enter....\n 1 for Rock \n 2 for paper \n 3 for scissor\n")
        if playerchoice not in ["1","2","3"]:
            print("you must enter 1,2, or 3.")
            return play_rps()
        player=int(playerchoice)
        if player<1 or player>3:
            sys.exit("Enter a valid option")
        computerchoice=random.choice("123")
        computer=int(computerchoice)
        print("")
        print("You choose"+" "+str(player))
        print("python choose" + " "+str(computer))

        if player==1 and computer==3:
            print("👍 you win !")
        elif player==2 and computer==1:
            print("👍 you win !")
        elif player==3 and computer==2:
            print("👍 you win !")
        elif player==computer:
            print("😂 Match Tie")
        else:
            print("🐍 Python wins")
        

        while True:
            playagain=input("\nplay again? \nY for yes \nQ for quit \n\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        
        
        else:
            print("Thank you for playing \n")
            sys.exit("Byee")
            
play_rps()































