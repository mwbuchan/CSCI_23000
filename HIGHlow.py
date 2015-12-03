''' HIGH low
    Created by Maggie Buchanan
    CSCI 23000
    10/16/15'''
# random integer from 1-100 is generated
import random
correct = random.randint(1,101)
# the first guess they have is 1 turn
turn = 1
keepGoing = True
# introduces user to game
print("Hi, welcome to the Great Number Debacle!")
print("I will think of a number from 1 to 100,")
print("and you must guess what I'm thinking of.")
user = input("What will be your first guess? ")
while keepGoing:
    try:
        # if the user's guess is less than the correct integer
        if int(user) < correct:
            user = int(input("Too low! Pick again! "))
            # add one to the number of guesses
            turn += 1
        # if the guess is greater than the correct integer
        elif int(user) > correct:
            user = int(input("Too high! Pick again! "))
            # add one to the number of guesses
            turn += 1
            keepGoing
        # if the user guesses the correct number    
        elif int(user) == correct:
            # break out of the loop
            keepGoing == False
    # if the user enters a value that can't be converted to an integer
    except ValueError:
        user = int(input("Is that even a number? Try to stick with integers from 1-100. "))
        turn += 1
        continue
        
        
turn = str(turn)
print("How did you know? You only took " + turn + " turns! Thanks for playing!")
      
