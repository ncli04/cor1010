import numpy as np

longstring = 

uniquechars = []
charset = []
for char in longstring:
   if char not in uniquechars:
        uniquechars.append(char)
        charset.append(char)

print("unique: ", len(uniquechars), uniquechars)
print("unique set:", len(uniquechars), charset)

print(charset[0])
charlist = []

for elem in charset:
    charset.append(elem)

charlist2 = list( charset )

print(charlist)
print(charlist2)
