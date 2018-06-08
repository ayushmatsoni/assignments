t=(1,2,45,3)
print(t)
##del t
#print(t)
l= [11,22,56]
b=tuple(l)
print(l)
print(b)
c=str(l[0])
d=str(b)
print(c)
print(d)

#min , max
tup=(45,568,45,78,32,54,1,12,14)
print(tup)
x=max(tup)
y=min(tup)
print(x)
print(y)

#sets
a1=set(tup)#pass list or a tuple
a2=set(t)
print("sets")
a3=a1|a2
a4=a1&a2
print(a3)
print(a4)
a3.add(4574)
print(a3)


#remove
print("a1 set=")
print(a1)
a1.pop()
a1.discard(12)
print(a1)
a1=set([1,2,3,4,5])
a2=set([2,3,4])
s3=a1<=a2
s4=a2<=a1
print(s3)
print(s4)

#dict

d= {'name':'ayush' ,'eng':18,
'  maths':45 ,
   'comp':56
   }
print(d)
print(d["name"])
d["eng"]=99
print(d["eng"])
#d.clear()
del d["eng"]
print(d)
del d
#print(d)