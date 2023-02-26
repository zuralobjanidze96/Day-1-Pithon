# factorial function
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n
# calling function
n = int(input("Enter the number: "))
factorialn = factorial(n)
print("factorial for the number",n, "is", factorialn)