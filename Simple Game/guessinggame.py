
#only have 3 tries to guess the answer
answer = "hello"
print("Time to guess the word!")
stopper = True
counter = 0

while stopper is True and counter is counter < 3:
    guess = input("Guess a word: ")
    counter += 1
    if (counter >= 3 and guess != answer):
        print ("Out of tries! Game over")

    if (counter <= 3 and guess == answer):
        print ("You guessed the word!")
        stopper = False
    
    else:
        stopper = True
        if (counter < 3):
            print("Wrong Answer! Try again!")
        elif(counter == 3 and stopper is True):
            print("Game Over! You run out of tries!")

        

  
