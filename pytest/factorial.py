import math
def factorial(x):
    return math.factorial(x)
print(factorial(5))


#We can directly loop over all the numbers for 1 to n and directly multiply the product.
def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod
 
if __name__ == '__main__':
    print(factorial(4))
    print(factorial(7))
    