''' Creater by Maggie Buchanan
    CSCI 23000
    10/09/15
    Change Maker
    I didn't know how to use modulus at all,
    so I made up a thing that probably doesn't work.
    don't know what I'm doing really please help me.
    '''

# price gets user input
price = input("How much does your purchase cost? ")
# price is converted to float, multiplied by 100, and converted to integer
price = int(float(price)*100)
# tender gets user input
tender = input("And with how much will you be paying? ")
# tender repeats the conversions that price underwent
tender = int(float(tender)*100)
# change gets tender minus price
change = tender - price
# change is sorted into bills and coins through division and conversion (I had no idea how to use modulus to make it do the right thing)
twenties = int(change/2000)
change = change - twenties*2000
tens = int(change/1000)
change = change - tens*1000
fives = int(change/500)
change = change - change*500
ones = int(change/100)
change = change - change*100
quarters = int(change/25)
change = change - change*25
dimes = int(change/10)
change = change - change*10
nickels = int(change*5)
change = change - change*5
pennies = change


# prints out all of the collected and calculated data

print("Price of the purchase: $" + str(float(price/100)))
print("Cash tendered: $" + str(float(change/100)))
print("Change: $" + str(float(change/100)))
print("Twenties: " + str(twenties))
print("Tens: " + str(tens))
print("Fives: " + str(fives))
print("Ones: " + str(ones))
print("Quarters: " + str(quarters))
print("Dimes: " + str(dimes))
print("Nickels: " + str(nickels))
print("Pennies: " + str(pennies))
print("Thanks for playing!")
