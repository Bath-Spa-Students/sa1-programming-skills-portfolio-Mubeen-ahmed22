#This is a welcome message
print("""Twinkle Twinkle little star
            How i wonder what you are""")
print("""Up above the worlds so high
            Like the diamond in the sky""")

print("""Jhonny Jhonny 
            Yes papa""")
print("""Eating sugar
             No papa""")

#Variables
x=10
y="bathspa"
print(x)
print(y)

x="whats your Name"
y="mubeen ahmed"
print(x)
print(y)

A = 1
B = 2
C= 3
D= 4
E = 5
print ( A,B,C,D,E)

name = "Mubeen Ahmed"
name = "bathspa"
print(name)

x = "bathspa"
print(type(x))

x = 5
y = "john"
print(x)
print(y)

x = 4
x = "sally"
print(x)


x = str(3)
y = int(3)
z = float(3) 
print (x,y,z)

x = 5
y = "bathspa"
print(type(x))
print(type(y))

x = "john"
x = 'john'
print( x,x)

#string concatenation through variables
message = 'Hello ' + 'my ' + 'name ' + 'is ' + 'mubeen'
print(message)

message = 'I ' + 'study ' + 'in ' + 'bathspa ' + 'university'
print(message)

#string concat through diff varaibles
a = "hello"
b = "world"
c = a + " " + b 
print(c)

a = "cars"
b = "are"
c = "cool"
print(a + " " + b + " " + c)

#string concat through print statement
print('hello ' + 'universe')

print('my ' + 'name ' + 'is ' + 'MUBEEN ' + 'AHMED')


#to get input from     ----------Input take by deafult string from user
name = input("Enter your surname: ")
print(name )

name = input("Where do you live? : ")
print(name )

#Type cast with integar
age = int(input("Enter Age : "))
print(age )


#performing calculations
print (3 + 7)
print (5-3)
print (30 *9)
print (40/2) #for floating point
print (60//2) #for integar

x = 3
y = 2
print(x + y)

x = 3
y = 2
z = 4
print((x + y)*z)

#operator precedence BODMAS ( bracket,order,division,multiplication,addition,subtraction)
print((2*3)/8 +(23+5))

#to write formulae in multiple lime we need back slash \
result = 6 * 2 + 4 * 3 \
 * 4 + 2 * 5

#end delimiter to remove new line, By deafult print will switch to another statement
name = "mubeen ahmed"
print (name , end =" " )
print ( "New print line message")

#\n and \t these are also known as escape sequnces 
print ("\n this line willl print on the next line")
print ("\t this is tabbed in ")

#formated output
name = "mubeen"
print (f" my name is {name }")


m = 4
n = 8

if n > m:
    print("n is greater than m")

y = 3
z = 2

if y > z:
    print("y is greater than z")


temperature = 60

if temperature < 40:
    print("little cold isnt it")
else:
    print("nice weather were having")

weight = 90

if weight < 150:
    print("muaaz is fat")
else:
    print("muaaz is still fat")


#if else if statements

earning = int(input("Enter your earning per year: "))
work_Experience = float (input("Enter your work Experience: " ))

if earning >= 30000:
 if work_Experience >= 2:
     print("Eligible for loan")
 else:
     print("Enter your work experience is less than 2 years")
else: 
    print("Sorry your earning is less than 30 k")


#elif
a = 44
b = 90
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



score = int (input("Enter your score: "))
if score > 90:
    print("you are smart so you passed")
elif score < 50:
    print("Try harder next time")
else:
    print("you are doing good")


score = int (input("Enter your score: "))
if score > 90:
    print("A")
elif score > 90:
    print("B")
elif score > 80:
    print("C")
elif score > 70: 
    print("D")
elif score > 60:
    print("E")
else:
    print("F")   

#local variables
def print_message():
    message ="Hello Students" #local variables
    print(message)
#calling function
print_message()




  
