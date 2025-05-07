# Name: Ivan Maldonado
# Date: May 6, 2025
# Description:This code asks the user for the current hour (in 24-hour format) and how many hours they want to wait, then calculates what the time will be when the alarm goes off.


currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = (currentTimeInt + waitTimeInt) % 24
print(finalTimeInt) 