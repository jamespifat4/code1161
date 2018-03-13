"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# This will print the following list of words 'what', 'does', 'this', 'line', 'do', '?' 
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # It printed the words in the brackets.

# It will perform the previous function as in line 12 and 15.
for word in some_words:
    print(word) # Every time I hit F5, it printed the some_words function in a list vertically. 

# I think it will print random words from the lsit on line 15.
for x in some_words:
    print(x) # Everytime I pressed F5 a word from the list was displayed in chronological order.

# I think it will print the list of words.
print(some_words) # It had printed the list of words exactly.

# I think it will print out some_words contain more than 3 words since the list - some_words has more than 3 words.
if len(some_words) > 3:
    print('some_words contains more than 3 words') # It printed out exactly has I said.

# After reading uname's function, I suspect the system will return my computer's specs. 
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) 
usefulFunction() # It displayed exactly what I stated, showcasing my device's specs.

