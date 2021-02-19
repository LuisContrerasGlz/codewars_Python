# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    isogram = True
    l = len(string)
    i = 0
    while (i < l and isogram):
        c = string[i]
        j = i+1
        while (j < l and isogram):
            if (c.lower() == string[j].lower()):
                isogram = False
            j = j+1
        i = i+1
    return isogram


# This kata is about converting numbers to their binary or hexadecimal representation:

# If a number is even, convert it to binary.
# If a number is odd, convert it to hex.

def evens_and_odds(n):
    conv = ""
    numero = n
    if (n % 2 == 0):
        while (numero != 0):
            digito = numero % 2
            conv = str(digito)+conv
            numero = int(numero / 2)
    else:
        while (numero != 0):
            digito = numero % 16
            if (digito < 10):
                conv = str(digito)+conv
            elif (digito == 10):
                conv = 'a'+conv
            elif (digito == 11):
                conv = 'b'+conv
            elif (digito == 12):
                conv = 'c'+conv
            elif (digito == 13):
                conv = 'd'+conv
            elif (digito == 14):
                conv = 'e'+conv
            elif (digito == 15):
                conv = 'f'+conv
            numero = int(numero / 16)
    return conv

# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.


def switcheroo(string):
    l = len(string)
    x = list(string)
    for i in range(0, len(x)):
        c = string[i]
        if (string[i] == "a"):
            x[i] = "b"
        elif (string[i] == "b"):
            x[i] = "a"

    string = "".join(x)
    return string

# Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.


def trouble(x, t):
    y = []
    l = len(x)
    y.append(x[0])
    pre = x[0]
    for i in range(1, l):
        if (pre+x[i] != t):
            y.append(x[i])
            pre = x[i]
    return y

# Given a mixed array of number and string representations of integers, add up the string integers and subtract this from the total of the non-string integers.


def div_con(x):
    # your code here
    stringSum = 0
    numSum = 0

    for i in range(len(x)):
        if type(x[i]) is str:
            stringSum = float(x[i]) + stringSum
        else:
            numSum = numSum + x[i]
    return numSum - stringSum
