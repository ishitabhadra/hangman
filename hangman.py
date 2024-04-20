import random

#check for duplicate guesses - 5th bullet point

words = ["dog", "python", "java", "elephant"]
print("Lets play Hangman!")


def hangman():
  global lives
  lives = 6
  global listOfGuesses
  listOfGuesses = []
  word = random.choice(words)
  newWord = list(word)
  userOutput = list(word)
  for i in range(len(word)):
    userOutput[i] = "-"
  print(userOutput)
  print("Lives left: 6")

  def guessLetter(lives, listOfGuesses):
    if newWord == userOutput:
      print("Game over!")
      quit()
    letterGuessed = input("Guess a letter:")
    listOfGuesses.append(letterGuessed)
    

    if letterGuessed.isalpha() and len(letterGuessed) == 1 and lives > 0:
      if letterGuessed in word:
        if newWord == userOutput:
          print("Game over!")
          quit()
        else:
          for i in range(len(word)):
            if letterGuessed == newWord[i]:
              userOutput[i] = letterGuessed
          print(userOutput)
          print("Lives left: " + str(lives))
          guessLetter(lives, listOfGuesses)
      else:
        lives = lives - 1
        if lives == 0:
          print(userOutput)
          print("Out of lives, game over!")
          quit()
        print(userOutput)
        print("Letter not found!")
        print("Lives left: " + str(lives))
        guessLetter(lives, listOfGuesses)
    else:
      print("Not  valid guess. Please enter a single letter")
      guessLetter(lives, listOfGuesses)

  guessLetter(lives, listOfGuesses)


hangman()
