#assignment 4

#question1
t=(1,2,45.888888,30.56,"ayushmat")
print(t)
l=len(t)
print("lenght = %d"%l)

#question2
tup=(45,568,45,78,32,54,1,12,14)
print(tup)
x=max(tup)
y=min(tup)
print(x)
print(y)
mul=1

#question3
l1=list((4,5,2,1,2))
for i in l1:
    ex=i
    mul=mul*ex
print("MULTIPLICATION=%.2f"%mul)


#SETS

#question1
a1=input("ENTER THE SET 1")
a2=input("ENTER THE SET 1")
a3=input("ENTER THE SET 1")
b1=input("ENTER THE SET 2")
b2=input("ENTER THE SET 2")
b3=input("ENTER THE SET 2")
b4=input("ENTER THE SET 2")
b5=input("ENTER THE SET 2")

set1=set([a1,a2,a3])
set2=set([b1,b2,b3,b4,b5])

ans1=(set1<=set2)
ans2=(set2<=set1)
print(ans1)
print(ans2)
ans3=set1&set2
print(ans3)
ans4=set1-set2
print(ans4)

#dictionary

#question1
name=input("enter name")
marks=input("enter marks")
d= {'name':name ,'marks':marks,}
print(d)

#question2


#question3
word="MISSISSIPPI"
m=word.count("M")
i=word.count("I")
s=word.count("S")
p=word.count("P")

print("M=%d  I=%d  S=%d P=%d  "%(m,i,s,p))
d2= {'NO OF M':m ,'NO OF I':i,'NO OF S':s ,'NO OF P':p}
print(d2)