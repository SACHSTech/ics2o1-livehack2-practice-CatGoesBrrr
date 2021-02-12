'''
-------------------------------------------------------------------------------
Name:       problem2.py
Purpose:  Vacation

Author:    Tan.C

Created:    date in 02/12/2021
------------------------------------------------------------------------------
'''
print("****** Vacation ******")

# get mark and earnings from user
mark = int(input("Mark: "))
earnings_before_the_summer = int(input("Earnings: "))

# output results
if mark >= 80 and earnings_before_the_summer >= 500:
  print("You can go to Europe!")

elif mark >= 80:
  print("You can go to California!")

else:
  print("Sorry, you have to stay home.")