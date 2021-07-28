'''Create a program that reads the length and width of a farmers field from the user in feet.
Display the area of the field in acres.

Hint:

There are 43,560 square feet in an acre

SQ=43560; (Squarefeet)

Formula = (length*width)/squarefeet'''

a=float(input())
b=float(input())
c=a*b/43560
d=round(c,2)
print("The area of the field is " + str(d) + " acres")
