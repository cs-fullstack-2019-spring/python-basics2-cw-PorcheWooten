def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()


# Create a random number. Print the number.
def problem1():
    import random
    randomNum = random.randint(0,5)
    print(randomNum)


# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def problem2():
    while (True):
        userInput = input("Enter something ")
        if userInput == "q":
            break


# Create a function that will loop until the user enters '0'. Ask the user to enter a positive integer number. Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.
def problem3():
    while (True):
        userInput2 = int(input("Enter a positive number "))
        for n in range (0,userInput2):
            print(n)
        if userInput2 == 0:
            break


# Create a function that creates a random number. Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit. If they don't get it right, tell them if their next guess has to be higher or lower.
def problem4():

    import random
    numGuess = random.randint(0,100)
    while(True):
        userInput = int(input("Enter a number from 0 to 100 "))
        if numGuess == userInput:
            break
        elif userInput > numGuess:
            print("LOWER!!")
        elif userInput < numGuess:
            print("HIGHER!!")
        # print(numGuess)




if __name__ == '__main__':
    main()
