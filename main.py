import random, time

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
   'coyote crow deer dog donkey duck eagle ferret fox frog goat '
   'goose hawk lion lizard llama mole monkey moose mouse mule newt '
   'otter owl panda parrot pigeon python rabbit ram rat raven '
   'rhino salmon seal shark sheep skunk sloth snake spider '
   'stork swan tiger toad trout turkey turtle weasel whale wolf '
   'wombat zebra ').split()

# Chosen animal
word = random.choice(words)
# List of guessed letters
guessedLetters = []
# Number of lives
lives = 6
# Index to print the hangman
hangmanIndex = 1

print("🌟Hangman🌟")
print()
print(HANGMANPICS[0])
print()
print("You are guessing the name of an animal")
print()

while True:
  time.sleep(1)
  letter = input("Choose a letter: ").lower()
  print()
  
  if letter in guessedLetters:
    print("You've already guessed that letter")
    continue
    
  guessedLetters.append(letter)
  
  if letter in word:
    print("Correct!")
  else:
    print("Nope, not in there.")
    lives -= 1
    print(HANGMANPICS[hangmanIndex])
    hangmanIndex += 1

  allLetters = True
  print()
  for i in word:
    if i in guessedLetters:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print()
    print(f"You won with {lives} left!")
    break
  
  if lives <= 0:
    print()
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print()
    print(f"{lives} left.")
    print()
   
