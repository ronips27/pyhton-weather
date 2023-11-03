import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    pyhthon_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal pyhthon_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerchoice = input(f"\n{name}, Enter..\n1. For Rock \n2. For Paper \n3. For Scissor\n\n")

        if playerchoice not in ['1','2','3']:
            print(f"{name}, You Must Enter 1,2, or 3")
            return play_rps 
        
        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, You chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n")
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal pyhthon_wins
            if player == 1 and computer == 3 :
                player_wins += 1
                return f"{name} You Win!"
            elif player == 2 and computer == 1 :
                player_wins += 1
                return f"{name} You Win!"
            elif player == 3 and computer == 2 :
                return f"{name} You Win!"
            elif player == computer:
                print("Tie Game!")
            else:
                print("Python Wins!")
                pyhthon_wins += 1   


        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name} Wins: {game_count}")
        print(f"\nComputer Wins: {game_count}")

        print(f"\nPlay Again {name}?")

        while True:
            playAgain = input("Y for Yes or \nQ to quit\n")
            if playAgain.lower not in ["y","q"]:
                continue
            else:
                break
        
        if playAgain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing")
            sys.exit(f"Bye {name}")
    
    return play_rps




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()

