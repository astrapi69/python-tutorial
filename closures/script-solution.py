# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. 
# That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

# your code goes here
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))