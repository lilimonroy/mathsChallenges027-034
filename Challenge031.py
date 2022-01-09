#----------* CHALLENGE 31 *----------
#Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work out the area of the circle (π*radius'2).

import math

radius = float(input("Enter the radius of a circle: "))

area = (math.pi * (radius**2))

print("The area of the circle is:",area)
