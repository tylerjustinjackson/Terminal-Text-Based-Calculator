"""
text calculator ask user for input and does calculation for user
will be able to handle powers mult div sub etc
if decimal inputed will output decimal else will output int
"""
def main():                                                                         #gets input
    calc_function = input("Calculation input: ")
    determineinput(calc_function)

def error():                                                                        #returns error message
    calcfunction = input("Invalid input, please reenter equation: ")
    determineinput(calcfunction)

def ending(x):
    if "no"  == x or "n" == x:
        main()
    elif "yes" == x or "y" == x: 
        print("Program quitting...")
    else:
        print("Invalid input. ", end="")
        final()
    
def final():
    finalinput=input("Are you finished? (Y/N) ").strip().lower()
    ending(finalinput)

def mult(x):                                                                        #multiplication
    number1,number2 = x.split("*")
    try:
        if "." in x:
            print(float(number1)*float(number2))
        else:
            print("The product is ",int(number1)*int(number2))
        final()
    except:
        error()

def div(x):                                                                             #division
    try:
        number1,number2 = x.split("/")
        if number2.strip() == "0":
            print("Answer is undefined")
            final()
        else:
            if "." in x:
                print(float(number1)/float(number2))
            else:
                print("The quotient is ",int(number1)/int(number2))
            final()
    except:
        error()

def sub(x):                                                                         #subtraction
    try:
        number1,number2 = x.split("-")
        if "." in x:
            print(float(number1)-float(number2))
        else:
            print("The difference is ",int(number1)-int(number2))
        final()
    except:
        error()

def add(x):                                                                        #additon
    try:
        number1,number2 = x.split("+")
        if "." in x:
            print(float(number1)+float(number2))
        else:
            print("The sum is ",int(number1)+int(number2))
        final()
    except:
        error()

def pow(x):                                                                         #powers/exponents
    try:
        number1,number2 = x.split("^")
        if "." in x:
            print(float(number1)**float(number2))
        else:
            print("The answer is ", end="")
            print(int(number1)**int(number2))
        final()
    except:
        error()

def determineinput(x):                                                              
    try:
        if "*" in x:
            mult(x)
        elif "/" in x:
            div(x)
        elif "-" in x:
            sub(x)
        elif "+" in x:
            add(x)
        elif "^" in x:
            pow(x)
        else:
            error(x)
    except:
        error()

if __name__ == '__main__':                                              #make sure it starts off running from file and not import
    main()