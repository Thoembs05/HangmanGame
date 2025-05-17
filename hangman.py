"""
Hangman Game
-------------
A simple command-line Hangman game in Python.

How to Play:
- The game randomly selects a word from a predefined list.
- You have 6 tries to guess the word by suggesting one letter at a time.
- If you guess a letter correctly, it is revealed in the word.
- If you guess incorrectly, you lose a try.
- The game ends when you either guess the word or run out of tries.

To run the game:
    python hangman.py
"""

import random

def display_hangman(tries):
    stages = [
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        _|_
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        _|_
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
        _|_
        ''',
        '''
         ------
         |    |
         |    O
         |   /|
         |    
         |
        _|_
        ''',
        '''
         ------
         |    |
         |    O
         |    |
         |    
         |
        _|_
        ''',
        '''
         ------
         |    |
         |    O
         |    
         |    
         |
        _|_
        ''',
        '''
         ------
         |    |
         |    
         |    
         |    
         |
        _|_
        '''
    ]
    print(stages[tries])

# Topics and word lists
word_topics = {
    'cartoon characters': [
        'spongebob', 'patrick', 'squidward', 'tom', 'jerry', 'mickey', 'minnie', 'donald', 'goofy', 'pluto',
        'simba', 'scar', 'stitch', 'lilo', 'elsa', 'anna', 'olaf', 'woody', 'buzz', 'shrek'
    ],
    'brainrot': [
        'sigma', 'gyatt', 'rizz', 'sus', 'yeet', 'slay', 'drip', 'vibe', 'noob', 'poggers',
        'simp', 'cap', 'bussin', 'bet', 'lit', 'flex', 'goofy', 'based', 'cringe', 'slaps'
    ],
    'music artists': [
        'beyonce', 'drake', 'adele', 'eminem', 'rihanna', 'taylor', 'weeknd', 'ed', 'billie', 'bruno',
        'kanye', 'ariana', 'dua', 'justin', 'shakira', 'usher', 'sza', 'olivia', 'lizzo', 'doja'
    ]
}

print('Select a topic:')
for idx, topic in enumerate(word_topics.keys(), 1):
    print(f'{idx}. {topic.title()}')
while True:
    try:
        topic_choice = int(input('Enter the number of your topic choice: '))
        if 1 <= topic_choice <= len(word_topics):
            topic = list(word_topics.keys())[topic_choice - 1]
            break
        else:
            print('Invalid choice. Try again.')
    except ValueError:
        print('Please enter a valid number.')

word_list = word_topics[topic]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ['_'] * word_length
guessed_letters = set()
tries = 6

print(f'Welcome to Hangman! Topic: {topic.title()}')

while tries > 0 and '_' in display:
    display_hangman(tries)
    print('\nWord:', ' '.join(display))
    print(f'Tries left: {tries}')
    guess = input('Guess a letter: ').lower()

    if not guess.isalpha() or len(guess) != 1:
        print('Please enter a single letter.')
        continue
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue

    guessed_letters.add(guess)
    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = guess
        print('Good guess!')
    else:
        tries -= 1
        print('Wrong guess!')

if '_' not in display:
    print(f'\nCongratulations! You guessed the word: {chosen_word}')
else:
    display_hangman(tries)
    print(f'\nGame over! The word was: {chosen_word}')
