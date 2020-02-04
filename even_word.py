# pedac 
# p - every character in a word must be in a word an even number of times 

# e- even_word('aabbbb') == 0
# even_word('aaabbbccc') == 3

# d -input:string
# output:number

# a-loop over a string and add every character to a dictionary
# - every character will begin with a value of one
# -add one every time the character repeats 
# - look for uneven values in the dictionary after we have looped through the word
# -if a value is uneven subtract by one one and store the number of times we subtract in a varibake 
# -return the variable 



def even_word(word):
    letters = {}
    uneven = 0
    for letter in word:
        if letter not in letters:
            letters[letter] = 1
        elif letter in letters:
            letters[letter] += 1
    
    for letter in letters:
        if letters[letter] % 2 == 1:
            uneven += 1 
    return uneven 
    
            
            
print(even_word('potato') == 2)
print(even_word('aabbbb') == 0)
