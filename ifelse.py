#write a python program to check given number is positive or negative
x=int(input("Enter a number:"))
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:                                           #elif:
    print(x,"is neither negative nor positive ")
