import pygame
import urllib.request
from classes.letter import Letter
from classes.slot import Slot

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((810, 720))
pygame.display.set_caption("Wordle Solver")

QWERTY_ALPHABET = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Colors
BLACK = (18, 18, 19)
TEXT_WHITE = (248, 240, 240)
WHITE = (129, 131, 132)
GRAY = (58, 58, 60)
YELLOW = (181, 159, 59)
GREEN = (83, 141, 78)

answers_url = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/c46f451920d5cf6326d550fb2d6abb1642717852/wordle-answers-alphabetical.txt"
guesses_url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/d7c9e02d45afd26e12a71b4564189a949c29e8a9/wordle-allowed-guesses.txt"

with urllib.request.urlopen(answers_url) as response:
    words1 = response.read().decode('utf-8').splitlines()
with urllib.request.urlopen(guesses_url) as response:
    words2 = response.read().decode('utf-8').splitlines()

all_words = sorted(set(words1 + words2))

possible_words = all_words

all_letters = list(QWERTY_ALPHABET)
possible_letters = [all_letters]*5
gray_letters = []


def set_slot_letter_color(letter, color):
    for ltr in letters:
        if ltr.get_letter() == letter:
            ltr.set_color(color)
            update_gray_letters(letter, color)


def update_gray_letters(letter, new_color):
    if new_color == GRAY and letter not in gray_letters:
        gray_letters.append(letter)
    elif new_color != GRAY and letter in gray_letters:
        gray_letters.remove(letter)

    update_possible_letters()


def update_possible_letters():
    global possible_letters
    # Start with all letters except gray ones
    possible_letters = [
        [letter for letter in all_letters if letter not in gray_letters]
        for _ in range(5)
    ]

    for i in range(5):
        letter = slots[i].get_letter()
        if not letter:
            continue

        color = slots[i].get_color()

        if color == GREEN:
            # Keep only the green letter for this slot
            possible_letters[i] = [letter]

        elif color == YELLOW:
            # Remove just that letter from this slot's possibilities
            possible_letters[i] = [
                l for l in possible_letters[i] if l != letter
            ]

    update_possible_words()


def update_possible_words():
    global possible_words

    # Collect all yellow letters from slots
    yellow_letters = [
        slots[i].get_letter().upper()
        for i in range(5)
        if slots[i].get_color() == YELLOW
    ]

    possible_words = [
        word for word in all_words
        if all(word[i].upper() in possible_letters[i] for i in range(5))
        and all(y in word.upper() for y in yellow_letters)
    ]

    print(f"Number of possible words: {len(possible_words)}. First 5: {possible_words[:5]}")


def add_letter_to_slot(letter):
    for i in range(5):
        if slots[i].get_letter() == "":
            slots[i].set_letter(letter)
            # When a letter is added to a slot, it becomes a gray letter
            update_gray_letters(letter, GRAY)
            break


slots = [Slot(1, x=160, y=25, callback=set_slot_letter_color),
         Slot(2, x=260, y=25, callback=set_slot_letter_color),
         Slot(3, x=360, y=25, callback=set_slot_letter_color),
         Slot(4, x=460, y=25, callback=set_slot_letter_color),
         Slot(5, x=560, y=25, callback=set_slot_letter_color)]
letters = []  # Letter objects


def main():
    x_offset = 10
    y_offset = 150
    x = x_offset
    y = y_offset
    for letter in QWERTY_ALPHABET:
        letters.append(Letter(letter=letter, x=x, y=y, left_click=add_letter_to_slot, right_click=update_gray_letters))
        x += 80

        if letter == "P":
            x = 35 + x_offset
            y = 100 + y_offset
        elif letter == "L":
            x = 115 + x_offset
            y = 200 + y_offset

    screen.fill(BLACK)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for letter in letters:
                letter.handle_event(event)
            for slot in slots:
                slot.handle_event(event)

        for letter in letters:
            letter.draw(screen)

        for slot in slots:
            slot.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
