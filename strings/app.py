my_string = "any text"
#print(f"{my_string}")

 #to uppercase
print(my_string.upper()) 

# to lower case
print(my_string.lower())

#firt leter upper case
print(my_string.capitalize())

# verify if its uppercase
print(my_string.isupper())

# verify id uts lowercase
print(my_string.islower())

# rmeove the space between
print(my_string.strip())

# replace 
print(my_string.replace("t","T", 1))

# how long is the text
print(len(my_string))

# show the index of an variable
print(my_string[-6:-2])

#show the first index of the word
print(my_string.index("text"))

#show if the text exist inside the string
x = "text" in my_string

print(x)

#_____________________________________________________________________________

#text with multiples of lines
my_string = """ line 1,\n line 2,\n line 3"""

print(my_string)