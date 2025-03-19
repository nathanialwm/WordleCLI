import requests
import random
from functools import lru_cache

# constants
BASE_URL = "https://wordle-words.onrender.com"
ENDPOINTS = ['easy', 'medium', 'hard']

@lru_cache(maxsize=None) #cache to prevent repeated requests
def fetch_words(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status() #check if the request was successful
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {endpoint}: {e}")
        return None

#simple reusable print    
def rules():
    print("You will have 6 attempts to guess the 5 letter word.\n"
    "a '-' means the letter is not in the word.\n"
    "a '/' means the letter is in the word but in the wrong position.\n"
    "if the position is correct the letter will be displayed\n\n"
    "Enter desired level: 'easy', 'medium', 'hard'")

# select difficulty, check for rules input, fetch word list
def select_level():
        
    user_input = input().strip().lower() 

    if user_input == "rules":
        rules()
        return
    elif user_input not in ENDPOINTS:
        print("Please enter a valid level")

    else:
        # Since user_input is one of the valid levels, fetch the word list once.
        print("Fetching word list...\n")
        words_list = fetch_words(f"{BASE_URL}/{user_input}")
        word = random.choice(words_list)
        return word

def guess(word): 
    user_guess = input().strip().lower()

    if len(user_guess) != 5:
        print("Please enter a 5 letter word")
        return None
    else:
        for i in range(5):
            if user_guess[i] == word[i]:
                print(user_guess[i], end="")
            elif user_guess[i] in word:
                print("/", end="")
            else:
                print("-", end="")
        print()
    return user_guess

def main():
    
    while True:
        print("Welcome to CLI Wordle\n"
            "Enter 'rules' if you need help\n"
            "Enter your desired level\n"
            "easy, medium, hard")
        word = None
        while word is None:
            word = select_level()
        print("Make your first guess\n"
        "-----")

        turn = 0 # keep track of the number of turns
        wincon = None
        while turn < 6:
            print(f"Turn {turn+1}")
            guess_result = guess(word)
            # Only count the turn if the guess is valid (i.e., exactly 5 letters)
            if guess_result is None:
                continue  # Do not increment turn
            turn += 1
            wincon = guess_result
            if wincon == word:
                break
        
        # if player loses
        if wincon != word:
            print(f"The word was {word}")          
        
        #cycle if player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break




if __name__ == "__main__":
    main()
