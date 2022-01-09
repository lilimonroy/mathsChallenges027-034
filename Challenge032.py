#----------* CHALLENGE 32 *----------
#Ask for the radius and the depth of a cylinder and work out the total volume (circle
#area*depth) rounded to three decimal places.

import math

radius = float(input("Enter the radius of a cylinder: "))
depth = float(input("Enter the depth of a cylinder: "))

areaCircle = math.pi*(radius**2)
volume = areaCircle*depth

print("The volume of the cylinder is:",volume,"[m3].")
