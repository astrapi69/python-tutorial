# Write a program using lambda functions to check if a number 
# in the given list is odd. Print "True" if the number is odd or "False" if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))