# q1 :
# Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .
# Hint: Dictionaries can be created either by using curly brackets or by using the dict  function.

Answer 1: 

d = {"a": 1, "b": 2}

Explanation 1: 

Using curly brackets is one way to create a dictionary.

Answer 2:

d = dict(a = 1, b = 2)

Explanation 2:

A dict  function is another way to create a dictionary. dict  is also used to convert other objects to a dictionary.

# -------------------------------------------------------------------------------------------------------------------------------

# q2 :
# Please complete the script so that it prints out the value of key b .
# d = {"a": 1, "b": 2}
# Expected output: 2

Answer: 

d = {"a": 1, "b": 2}
print(d["b"])  

# -----------------------------------------------------------------------------------------------------------------------------------

# q3 :
# Calculate the sum of the values of keys a  and b .
# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 3

Answer: 

d = {"a": 1, "b": 2, "c": 3}
print(d["b"] + d["a"])

# ------------------------------------------------------------------------------------------------------------------------------------

# q4 :
# Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.
# d = {"a": 1, "b": 2}
# Expected output: {'a': 1, 'c': 3, 'b': 2} 

Answer: 

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)
# ------------------------------------------------------------------------------------------------------------------------------------------

# q5:
# Complete the script so that it prints out the second item of the list.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: b

Answer: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# q6 :
# Complete the script so that it prints out letter i  using negative indexing.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: i 

Answer: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# q7:
# Complete the script so that it prints out a list slice containing the last three items of list letters .
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: ['h', 'i', 'j'] 

Answer: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# q8:
# Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: ['a', 'c', 'e', 'g', 'i'] 

Answer: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
