import random
import time
import sys
import os
from cards import TAROT_DECK

# --- COLORS ---
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def type_print(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_header():
    # os.system('clear') # We commented this out so you can see the history
    print(CYAN + BOLD + "\n" + "="*50)
    print("🔮 TERMINAL TAROT 🔮".center(50))
    print("="*50 + RESET + "\n")

def analyze_question(question):

    
    """Reads the question and figures out the category."""
    # This strips out punctuation and splits the sentence into individual words
    words = question.lower().replace("?", "").replace("!", "").replace(".", "").split()
    
    # Check for Study words
    if any(word in words for word in ["exam", "exams", "study", "pass", "test", "grade", "school", "college", "class"]):
        return "study"
    
    # Check for Money words
    elif any(word in words for word in ["money", "job", "rich", "work", "career", "boss", "salary", "pay"]):
        return "money"
    
    # Check for Love words
    elif any(word in words for word in ["love", "crush", "date", "dating", "ex", "relationship", "text"]):
        return "love"
    
    # If it doesn't match any of those, it goes to General
    else:
        return "general"

def read_fortune():
    print(CYAN + "-"*50 + RESET)
    question = input(BOLD + "Ask the universe a question: " + RESET)
    
    if not question.strip():
        question = "What do I need to know right now?"
        print(f"\n{YELLOW}You stayed silent. The cards will speak on your general vibe.{RESET}")
    else:
        print(f"\nYou asked: {YELLOW}'{question}'{RESET}")

    # Analyze the question
    category = analyze_question(question)
    print("\n" + MAGENTA + "Shuffling the deck..." + RESET)
    time.sleep(1.5)
    print(GREEN + f"The cards have chosen a path for you ({category.upper()}).\n" + RESET)
    time.sleep(1)

    # Pick a card from the specific category
    matching_cards = [card for card in TAROT_DECK if card["category"] == category]
    
    # If no cards match (shouldn't happen), fall back to general
    if not matching_cards:
        matching_cards = [card for card in TAROT_DECK if card["category"] == "general"]

    drawn_card = random.choice(matching_cards)

    # Print the result
    print(YELLOW + BOLD + f"Card Drawn: {drawn_card['name']}" + RESET)
    type_print(f"  {GREEN}Meaning:{RESET} {drawn_card['meaning']}", 0.02)
    type_print(f"  {CYAN}Advice:{RESET} {drawn_card['advice']}", 0.02)
    
    print(CYAN + "\n" + "="*50)
    print("The universe has spoken.".center(50))
    print("="*50 + RESET + "\n")

def main():
    print_header()
    read_fortune()
    
    while True:
        again = input(BOLD + "Would you like another reading? (y/n): " + RESET).lower().strip()
        if again == 'y':
            print("\n")
            read_fortune()
        elif again == 'n':
            print(MAGENTA + "\nFarewell. Go touch grass.\n" + RESET)
            break
        else:
            print("Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()
