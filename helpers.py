def alphabet_position(char):
    #This funciton is modified from the original assignment. If it
    #is critical to only have the original function then the following:
    #modifications should occur (additional changes will be needed in
    #other funcitons as well): change all refs to char to letter
    #delete elif condition
    #delete outer if isinstance
    #If given a letter, determine its zero-based position within the
    #alphabet. If given an integer, return the letter at that position
    alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   #test string
    if isinstance(char,str):    #if char is string
        if char.islower():      #normalize to uppercase
            char = char.upper()
        return alphabetString.find(char)    #Return the index of char
                                            #in the alphabetString
    elif isinstance(char,int):              #if char is integer
        return alphabetString[char%26]      #return the letter at that
                                            #index in the alphabetString


def rotate_character(char, rot):
    #Given a character string (char) of length 1 and integer (rot)
    #return a new character that has been rotated the rot number of
    #places.
    if not char.isalpha():   #If char is not alphabetical, return the same
        return char
    else:   #the new character is the character that results from
            #rotation + the original character's position wrapping back
            #to beginning if it is > 25. So inner alpha_pos call is getting
            #postion of original character, and outer call is getting
            #letter after rotation
        new_char = alphabet_position((alphabet_position(char)+rot)%26)
        if char.islower():
            new_char = new_char.lower()
        return new_char
