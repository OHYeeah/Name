while True:
    try:
        a = int(input ("Zahl 1: ")) #int a
        break
    except ValueError:
        print ("no good")
while True:
    try:
        b = int(input ("Zahl 2: ")) #int b
        break
    except ValueError:
        print("nur Zahlen eingeben bitte")

print ("Sum a+b = ", a+b)
print ("Dif a-b = ", a-b)
print ("Dif b-a = ", b-a)
print ("Dif b-a =", b-a)
print ("Pro a*b = " , a*b)

if a == 0 and b != 0:
    print ("Quo a/b = ",a/b)
    
if a != 0 and b == 0:
    print ("Quo b/a = ", b/a)
    
while  b == 0 or a == 0:
    print ("DIV 0!")
    b = int(input ("neue Zahl 2 eingeben:"))
    a = int(input ("neue Zahl 1 eingeben:"))
    

print ("Quo a/b = ",a/b)
print ("Quo b/a = ",a/b)