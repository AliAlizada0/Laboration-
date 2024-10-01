import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "No one won!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_score += 1
            return "***You Win***"
        else:
            self.computer_score += 1
            return "You lost!"

def main():
    game = RockPaperScissors()
    match_count = 0

    while True:
        print("""
1.rock
2.paper
3.scissors
4.exit
""")
        user_input = input("Please select an option: ").lower()

        if user_input in ["1", "rock"]:
            user_choice = "rock"
        elif user_input in ["2", "paper"]:
            user_choice = "paper"
        elif user_input in ["3", "scissors"]:
            user_choice = "scissors"
        elif user_input in ["4", "exit"]:
            break
        else:
            print("Invalid choice, please try again.")
            continue

        computer_choice = game.get_computer_choice()
        result = game.determine_winner(user_choice, computer_choice)
        match_count += 1

        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        print(result)
        print(f"Score: You {game.user_score} - {game.computer_score} Computer")
        print("\n*********************************************\n")

        if match_count == 3:
            continue_game = input("Do you want to continue playing? (yes/no): ").lower()
            if continue_game != "yes":
                break
            match_count = 0
if __name__ == "__main__":
    main() 