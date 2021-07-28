'''In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG).
In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). 
Use your research skills to determine how to convert from MPG to L/100 km. 
Then create a program that reads a value from the user in American units and displays the equivalent fuel efficiency in Canadian units.

Note:

Formula is --> 282.48 / fuel efficiency in MPG.'''

a=int(input())
print(round(282.48/a,2))
