### list ###
print("assigning elements to different lists")
list1=[23,65,12,89]
list2=[89,9,22,199,562]
x=1
y=2
z=0
n=int(input("enter 1 to append list2 to list2 and else press any number"))
if n==1:
     x=list1
     y=list2
     z=len(list2)
else:
     x=list2
     y=list1
     z=len(list1)
for i in range(z):
     x.append(y[i])

print(x)
