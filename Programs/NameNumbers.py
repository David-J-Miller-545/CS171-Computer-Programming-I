# Author: David Miller
# Date: 2/15/2023
# Program Name: NameNumbers
# Purpose: In Numerology, every name has a number between 1 and 9 related to it.
#          This program will ask the user for a name, then calculate the user's name number.
#          Once it knows the name number it can predict things about the person.


# Define required function(s) under this line
def sumDigits(number):
    sumD = number
    while sumD > 9 : # loops until the sum is less than 10
        number = str(sumD) # sets the number to a string to iterate through the for loop
        sumD = 0
        for x in number: # For loop that iterates through the string adding each digit/char together
            sumD += int(x)
    return sumD

def nameNumber(name):
    nums = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 8, "g" : 3, "h" : 5, "i" : 1,
    "j" : 1, "k" : 2, "l" : 3, "m" : 4, "n" : 5, "o" : 7, "p" : 8, "q" : 1, "r" : 2, 
    "s" : 3, "t" : 4, "u" : 6, "v" : 6, "w" : 6, "x" : 5, "y" : 1, "z" : 7}
    sumNum = 0 # declares the variable sumNum but also function returns this if name is invalid
    for x in name: # For loop that traverses the string name
        try:  # This is to try to key in the char x if it is in there
            sumNum += nums[x.lower()]  # Gathers a sum of all of the numbers in the name char by char
        except KeyError:  # There was a char that was not a letter
            sumNum += 0
    return sumDigits(sumNum)   # returns the return of the function sumDigits with the input of sumNum

def prediction(number):
    predict = {1 : "A person who is successful in personal ambitions.", 2 : "A gentle and artistic person.",
    3 : "A success in their professional career.", 4 : "An unlucky person who much put in extra work for success.",
    5 : "A lucky person who leads an unconventional life.", 6 : "A person who commands the respect of others.",
    7 : "A person who has a strong inner spirit.", 8 : "A person who is misunderstood by others and is not respected for their success.",
    9 : "A person who is more successful in matters of the material than spiritual."}
    
    try: # tries to key in the number to the dictionary and return its result
        return predict[number]
    except KeyError:  # number was not in the dictionary (mainly 0 or sum bug) and returns the string "Invalid Input"
        return "Invalid Input"


# The main script
if __name__ == "__main__":
    # code for the main script goes under this line, all indented
    print("Welcome to Name Number Generator")
    userName = input("Enter Your Name: ")
    nameNum = nameNumber(userName)
    print("Your Name Number is", nameNum)
    print("We predict you are:\n" + prediction(nameNum))