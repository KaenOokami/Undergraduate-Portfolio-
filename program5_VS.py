DB = float(input("Enter the Decible Level: "))

Jackhammer = 130

GasLawnmower = 106

AlarmClock = 70

QuietRoom = 40

if (DB <= QuietRoom):
  print ("The current noise level is quite silent akin to a quiet room or quieter")

elif (DB <= AlarmClock and DB > QuietRoom):
  print ("The current noise level is louder than a Quiet Room and at most as loud as an Alarm Clock")

elif (DB <= GasLawnmower and DB > AlarmClock):
  print ("The current noise level is quite loud louder than an alarm clock and at most as loud as a Gas Lawnmower")

elif (DB <= Jackhammer and DB > GasLawnmower):
  print ("The current noise level is really loud louder than a Gas Lawnmower and as loud as a Jackhammer")
