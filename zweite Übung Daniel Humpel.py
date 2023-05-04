a = int(input ("Zahl 1: ")) #int a
b = int(input ("Zahl 2: ")) #int b

print ("Sum = ", a+b)
print ("Dif= ", a-b)
print ("Pro = " , a*b)

if a == 0 or b == 0:
    print("DIV 0!")
    if a == 0: print("neue Zahl 1 eingeben")
    if b == 0: print("neue Zahl 2 eingeben")

else:
    print ("Quo = ",a/b)
