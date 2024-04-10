import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp >= 0 and timestamp < 12):
    print("good morning")
elif(timestamp >= 12 and timestamp < 17):
    print("good afternoon")
elif(timestamp >= 17 and timestamp < 0):
    print("good evening")       