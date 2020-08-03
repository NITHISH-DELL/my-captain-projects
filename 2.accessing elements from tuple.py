###  tuple ###

tuple=("helen","john","wane","april","ben","tony")
print("the total lenght is:",len(tuple))
n=int(input("enter the index to access the element"))

if n>=len(tuple):
     print("index out of range")
else:
     print(tuple[n])
