print("Welcome to pizza delivery")
size=input("Which size?")
pepp=input("pepp ?")
cheese=input("extra cheese?")
bill=0

if size == "S":
    bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
else:
    print("Wrong input")
if pepp=="Y":
    if size=="S":
        bill +=2
    elif size=="M" or size=="L":
        bill +=3
if cheese=="Y":
    bill +=1
print(f"Total bill is {bill}") 
