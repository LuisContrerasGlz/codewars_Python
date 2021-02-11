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
