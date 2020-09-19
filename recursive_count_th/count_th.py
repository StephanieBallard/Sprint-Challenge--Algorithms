'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#### 3. Use recursion to complete the `count_th()` function _(3 points)_
# Inside the `recursive_count_th` directory you'll find the `count_th.py` file. 
# In this file, please add your recursive implementation to the `count_th()` method following these rules:

# * Your function should take in a signle parameter (a string `word`)
# * Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
# * Your function must utilize recursion. 
# * It cannot contain any loops.

# Run `python test_count_th.py` to run the tests for your `count_th()` function to ensure that your implementation is correct.

# for character in characters if th appear add one to the count

# Recursive characterization of the operation of counting the occurrences of the character c in the string s:

# if s is the empty string "", then return 0;
# otherwise, if the first character of s is equal to c, then return 1 plus the number of occurrences of c in the string equal to s without the first character;
# otherwise (i.e., if the first character of s is different from c), return the number of occurrences of c in the string equal to s without the first character.
# Implementation:

# public static int countChars(String s, char c) {
#   if (s.length() == 0)
#     return 0;
#   else if (s.charAt(0) == c)
#     return 1 + countChars(s.substring(1), c);
#   else
#     return countChars(s.substring(1), c);
# }

def count_th(word):
    if len(word) <= 1:
        return 0
    elif word[0] == "t" and word[1] == "h":
        word = word[2:]
        return 1 + count_th(word)
    else:
        word = word[1:]
        return count_th(word)
    
print(count_th('teeth'))