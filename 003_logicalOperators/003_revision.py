import math

#Basic Logical Operators
print("......................................................................")
print("Basic Logical Operators")

#Power of two
if False:
    n = 3
    result = 1

    while(n > result):
        result *= 2
    
    if(result == n):
        print(f"{n} is a power of two")
    else:
        print(f"{n} is not a power of two")

#Water bottles
if False:
    numBottles = 9
    numExchange = 3

    total = numBottles
    emptyBottles = numBottles

    while(emptyBottles >= numExchange):
        remainder = emptyBottles % numExchange
        numBottles = int(math.floor(emptyBottles / numExchange))

        total += numBottles
        emptyBottles = numBottles + remainder
    
    print(f"Number of water bottles you can drink is: {total}")

#Fizz buzz
if False:
    aStr = []

    for i in range(1, 21):
        tStr = ""

        if(i%3 == 0):
            tStr += "Fizz"
        
        if(i%5 == 0):
            tStr += "Buzz"
        
        if(tStr == ""):
            tStr = str(i)
        
        aStr.append(tStr)
    
    print(f"{aStr}")


print("-End of script-")