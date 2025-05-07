# Name: Ivan Maldonado
# Date: May 6, 2025
# Description:This code is like the first time and again asks the user for the current hour (in 24-hour format) and how many hours they want to wait, then calculates what the time will be when the alarm goes off.


str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time)
print(time_when_alarm_go_off)
