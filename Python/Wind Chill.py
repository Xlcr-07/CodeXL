'''When the wind blows in cold weather, the air feels even colder than it actually is because the movement of the air increases the rate of cooling for warm
objects, like people. This effect is known as wind chill. In 2016, Jammu and Kashmir, the Delhi and the Himachal Pradesh adopted the following formula for computing the wind chill index.
Within the formula Ta is the air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in degrees Fahrenheit and wind speeds in miles per hour.

WCI = 13.12 + 0.6215Ta - 11.37V power 0.16 + 0.3965Ta V power 0.16

Write a program that begins by reading the air temperature and wind speed from
the user. Once these values have been read your program should display the wind
chill index rounded to the closest integer. The wind chill index is only considered
valid for m temperatures less than or equal to 10 degrees Celsius and wind speeds
exceeding 4.8 kilometers per hour.'''

a=float(input())
b=float(input())
p=b**(0.16)
print("Windchill is",round(13.12+(0.6215*a)-(11.37*p)+(0.3965*a*p),2))
