#### Fibonacci numbers ####


def fibonacci(n):
     print("the fibonacci numbers for",n,"numbers")
     i=0
     j=1
     print(i)
     print(j)
     for x in range(n):
          g=i+j
          print(g)
          i=j
          j=g
n=int(input("enter the number to get the fibonacci value upto the n numbers"))
fibonacci(n)
