Chance = int(input("Enter your Guess from 1 - 100: "))

for n in range(Chance,Chance + 10):
  if (Chance == 45):
    print ("YOU WIN! The Secret Number is 45")
    exit()
  else:
    print ("WRONG! TRY AGAIN!")
    n = n + 1
    Chance = int(input("Enter your Guess from 1 - 100: "))

print ("OUT OF CHANCES YOU LOOSE!")
