a=8
print(int(a))
b=8.0
print(type(b))
c="hello"
print(type(c))
a=2+3j
print(type(a))
print(isinstance(a,complex))
print(isinstance(b,str))
print(c.capitalize())
print(c.upper())
print(c.islower())
print(len("asdfghjk"))

s="Hello,there,Welcome,to,Acadview"
print(s.split("e"))

print("*********************************")
l=[999,22,3000,41,53,36] #mutable   list
t=() #non immutable tuple
d={}#mutable dict
print(l[1])
list=["happy",l] #list within list
print(list[1][2])
l.append(6)
print(l)
l.pop()
print(l)
l.insert(2,66)
print(l)
l.reverse()
print(l)
l.sort()
print(str(l))

ab=["aa","as","qa","aa","aa"]
ab.sort()
print(ab)
a="hello"
b=999
print(a+str(b))
x=ab.count("aa")
print(x)






