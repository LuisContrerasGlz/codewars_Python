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
