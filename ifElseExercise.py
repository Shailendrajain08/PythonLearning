import time
# timestamp = int(time.strftime('%H'))
timestamp =  int(input("enter hours: "))
print(timestamp)

if(timestamp >= 0 and timestamp < 12):
    print("good morning")
elif(timestamp >= 12 and timestamp < 18):
    print("good afternoon")
elif(timestamp >= 18 and timestamp < 24):
    print("good evening")       