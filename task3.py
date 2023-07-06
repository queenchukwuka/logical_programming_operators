swim_time = int(input("Enter total time for swimming in minutes: "))
print(swim_time)

cycl_time = int(input("Enter total time for cycling in minutes: "))
print(cycl_time)

run_time = int (input("Enter total time for running in minutes: "))
print(run_time)

total_time = swim_time + cycl_time + run_time
print(total_time)

if total_time < 100:                           # competition is completed within 100 minutes (ie., the qualifying time)
    print("Provincial colours")
elif total_time > 100 and total_time <= 105:   # competition is completed within 5 minutes of the qualifying time 
    print("Provincial Half colours")
elif total_time > 100 and total_time <= 110:    # competition is completed within 10 minutes of the qualifying time
    print("Provincial scroll")
elif total_time > 110:                          # competition is completed after 10 minutes of the qualifying time
    print("No award")