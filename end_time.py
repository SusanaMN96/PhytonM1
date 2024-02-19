hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour_to_min = hour*60
total_time_min = hour_to_min + mins + dura

min_to_hour = (mins+dura)/60
total_time_hour = int(min_to_hour + hour)

total_hour = total_time_hour%24
total_min = total_time_min%60


print(str(total_hour)+":"+str(total_min))
# Write your code here.
