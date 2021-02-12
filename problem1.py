'''
-------------------------------------------------------------------------------
Name:       problem1.py
Purpose:  Determines Right-angled Triangles

Author:    Tan.C

Created:    date in 02/12/2021
------------------------------------------------------------------------------
'''
print("****** Right-angled Triangles ******")

# get side lengths from user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# side lengths squared
sq1 = side1**2
sq2 = side2**2
sq3 = side3**2

# output results
print(" ")
if sq1 + sq2 == sq3 or sq1 + sq3 == sq2 or sq2 + sq3 == sq1:
  print("The triangle with side lengths " + str(side1) + ", " + str(side2) + ", " + str(side3) + " form a right-angled triangle")

else:
  print("The triangle with side lengths " + str(side1) + ", " + str(side2) + ", " + str(side3) + " do not form a right-angled triangle")