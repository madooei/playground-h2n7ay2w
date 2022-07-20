# EFFECTS: return value is the n!
def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod
  
# Print n! for n={0,1,2,3,4,5}
for n in range(6):
    print("{}! = {}".format(n,factorial(n)))