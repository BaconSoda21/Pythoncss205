# Name: Ivan Maldonado
# Date: May 13, 2025
# Description: This code uses numbers between 1 to 50 to then print out there mutiples. 


for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both")
    elif num % 3 == 0:
        print("Divisible by three")
    elif num % 5 == 0:
        print("Divisible by five")
    else:
        print(num)


