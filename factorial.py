def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = int(input("enter a number : "))

if num<0:
  print("sorry, factorial cannot be negative")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print("the factor of ", num, "is",recur_factorial(num))