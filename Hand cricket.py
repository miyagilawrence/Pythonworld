import random

print("All the best. Play as long as you can")
balls = 1
count = True
total = 0
count = 1
while (count,balls,1):
    user = int(input("Enter number\n"))
    print("You've inputed", user ,"\n")
    comp = (random.randint(1,6))
    print("Computer chose", comp , "\n")
    if (comp == user):
        print("You lose. The computer also chose a" , comp,"\n")
        break
    else:
        total = total + user
        print(" Your total is now" , total)
print("Your score is",total)
if total>=100:
    print("Hurrah!! You scored a century")
elif total>=50 and total<100:
    print("A gritty 50 mate. Well played")
else:
    print("Better luck next time champ")
    
