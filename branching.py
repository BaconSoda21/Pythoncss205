# Name: Ivan Maldonado
# Date: May 6, 2025
# Description: This script asks the user for a year (ex: when a time traveler is from) and prints a different message based on the time period:


# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print("Woah, that's the past!")
elif 1900 < year > 1900 < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!")
