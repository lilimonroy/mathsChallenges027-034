#----------* CHALLENGE 29 *----------
#Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.
import math

number = float(input(("Enter a number over 500: ")))

total = math.sqrt(number)

print(round(total,2))


