#IF ELSE CONDITION

#question1
year=int(input("ENTER ANY YEAR-> "))
print("")
if int(year)%4 == 0 :
    print("YEAR IS A LEAP YEAR   ")
else :
    print("YEAR IS NOT A LEAP YEAR  ")

#question2
l=int(input("ENTER LENGTH-> "))
b=int(input("ENTER BREADTH-> "))
if int(l)==int(b):
    print("THIS IS A SQUARE")
else :
    print("REACTANGLE")

#question3
a1=int(input("ENTER AGE OF A-> "))
a2=int(input("ENTER AGE OF B-> "))
a3=int(input("ENTER AGE OF C-> "))

if int(a1)<int(a2) and a1<a3:
    print("A IS YOUNGEST")
elif int(a2) < int(a3) and a2 <a1 :
    print("B IS YOUNGEST")
elif a3<a1 and a3<a2:
    print("C IS YOUNGEST")

if int(a1)>int(a2) and a1>a3:
    print("A IS OLDEST")
elif int(a2) > int(a3) and a2 >a1 :
    print("B IS OLDEST")
elif a3>a1 and a3>a2:
    print("C IS OLDEST")

elif a1 == a2 and a2 == a3:
    print("EQUAL AGES")
else:
    print("WRONG AGES")


#question4
points=int(input("ENTER POINTS -> "))
if points<200 :
    if points>1 and points<=50 :
        print("SORRY ! NO PRIZE WON")
    if points > 50 and points <= 150:
        print("CONGRATULATIONS! YOU HAVE WON WOODEN DOG! ")
    if points > 150 and points <= 180:
        print("CONGRATULATIONS! YOU HAVE WON BOOK")
    if points > 180 and points <=200:
        print("CONGRATULATIONS! YOU HAVE WON CHOCLATES!")
else :
    print("WRONG VALUE OF POINTS ENTERED")

#question5
tc=0
q=int(input("ENTER THE QUANITY-> "))
print("THE ARTICLE PURCHASED COST 100 PER PIECE")
if int(q)>1000:

    tc=(q*100)-(0.10*q*100)
    print("TOTAL COST = %.3f"%(tc))
else:
    tc = (q*100)
    print("TOTAL COST = %.3f" % (tc))