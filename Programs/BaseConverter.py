# HEADER COMMENT HERE


# DEFINE YOUR FUNCTIONS HERE
'''
Function Purpose:
Parameters:
Output: 
'''
def convertToBase(number, base):
    div = int(number / base)
    new = ''
    if not (div == 0):
        new += convertToBase(div, base) + str(number % base)
    else:
        new += str(number % base)
    return new
        
# The main routine here, after this line
if __name__ == "__main__" :
    while True:
        try:
            number = int(input("Enter an decimal integer: "))
        except ValueError:
            print("Invalid input: an integer value was expected. Try again.")
        try:
            base = int(input("Enter an the base you would like to convert to: "))
        except ValueError:
            print("Invalid input: an integer value was expected. Try again.")
        print(f"The equivalent of {number} in base {base} is {convertToBase(number, base)}")
        anotherNum = input("Do you have another number to convert (Y / N)? ")
        if anotherNum.lower() == "y":
            pass
        else:
            break
