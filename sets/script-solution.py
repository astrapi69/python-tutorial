# In the exercise below, use the given lists to print out a set containing all the participants from event A which did not attend event B
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

setA = set(a)
setB = set(b)

allPartipitiantsA = setA.difference(setB)

print(allPartipitiantsA)