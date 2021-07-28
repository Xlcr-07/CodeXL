'''Write a program to display a grocery bill of the product purchased in the small market by John by getting following input from the user .
Get the product name Get the price of the product(Price per Unit) Get the quantity of the product purchased.

Input and Output Format:

Refer sample input and output for formatting specification.

All float values are displayed correct to 2 decimal places.

All text in bold corresponds to input and the rest corresponds to output.'''

a=input()
b=float(input())
c=int(input())
print("Product Details")
print(a)
print(b)
print(c)
print("Bill: {:.2f}".format(b*c))
