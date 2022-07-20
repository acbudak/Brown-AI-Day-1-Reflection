
condition=input('İf you want to convert hours into minutes type hours otherwise in order to covert minutes into hours type minutes:')


if condition =="hours":
    hours = int(input("Please enter hours:"))
    minutes = hours * 60
    print(str(minutes) +" Minutes")


elif condition =="minutes":
     minutes = int(input("Please enter minutes:"))
     hours = minutes/60
     print(str(hours) +" hours")






