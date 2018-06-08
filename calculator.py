print("Select choice.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    res=num1+num2
    print(num1,"+",num2,"= %.2f"%(res))

elif choice == '2':
    res=num1-num2
    print(num1,"-",num2,"= %.2f"%(res))

elif choice == '3':
    res=num1*num2
    print(num1,"*",num2,"= %.2f"%(res))

elif choice == '4':
   res=num1%num2
   print(num1,"/",num2,"= %.2f"%(res))
else:
   print("Invalid input")
