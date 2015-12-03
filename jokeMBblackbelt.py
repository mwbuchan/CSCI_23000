''' The goal here is to tell a sweet knock knock joke
    Created by Maggie Buchanan
    for CSCI 23000
    Jennifer Emery is a beautiful human for helping me when I have all the errors
    '''

# I'm going to ask for the user's name
name = input("What is your name? ")

# I'm asking the user if they want to hear a knock knock joke
answer = input("Hi " + name + ", do you want to hear a knock knock joke? ")

# If they say 'no', I'm going to tell the joke anyway and allow them to respond
if answer == ("yes"):
    who = input("Awesome! Knock knock! ")
else:
    who = input("Too bad! Knock knock! ")

# I want the user to say 'Who's there?', so I'll correct them if they don't
while who != ("whos there?"):
    who = input("No, this is a knock knock joke, so say 'whos there?' ")
else:
    response = input("Little old lady! ")

# I want the user to say 'Little old lady who?' in some way, so I will correct the user if they don't
while response != ("little old lady who?"):
    response = input("No, you're supposed to say 'Little old lady who?' You don't understand knock knock jokes, do you? ")
else:
    print("I didn't know you could yodel! Thanks for being patient!")
