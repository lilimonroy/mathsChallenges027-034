#----------* CHALLENGE 34 *----------
#Display the following message:

#1)Square
#2)Triangle
#Enter a number

#If the user enters 1, then it should ask them for the length of one of its sides and display the
#area. If they select 2, it should ask for the base and height of the triangle and display the area. If
#they type in anything else, it should give them a suitable error message.

import math

print("*****Choose an option******")
print("1)Square\n2)Trinagle")

option = int(input("Enter an option [1 or 2]: "))

if option == 1:
    lenght = int(input("What's the lenght size of one of the sides of the square?: "))
    print("The area of the square is:",lenght*4)
elif option == 2:
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = (base * height)/2
    print("The area of the triangle is: ",area)