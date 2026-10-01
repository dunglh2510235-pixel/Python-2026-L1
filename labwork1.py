#Q1

p = (int(input("Enter circle radius? ")))
print ("Circle area = ", 3.14*p**2)

#Q2

p = (int(input("Enter the temperature in Celsius? ")))
print ("Circle area = ", 1.8*p+32)

#Q3


p = (int(input("Enter a number? ")))
for i in range(2, p):
    if p % i == 0:
        print (p, "is not a prime number")
        break
else:
    print (p, "is a prime number")


p = (int(input("Enter a number? ")))

if p <= 1:
    print (p, "is not a prime number")
else:
    for i in range(2, p):
        if p % i == 0:
            print (p, "is not a prime number")
        break
    else:
        print (p, "is a prime number")


#Q4

sum = 0

p = (int(input("Enter a number? ")))
for i in range(1, p):
    if p % i == 0:
        sum = sum+i

if sum == p:
    print (p, "is a perfect number")
else:
    print (p,"is not a perfect number")


#Q5

list = ["yellow", "blue", "Red", "gray"]

p = (str(input("What is your favorite color? ")))

for i in range (3):
    if list[i] == p:
        print("Your color is at index", i+1,  "in my list")
        break
else:
    print("Sorry, I could not find your color")


#Q6

range1 = range(0, 7, 1)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)

print(list(range1))
print(list(range2))
print(list(range3))
print(list(range4))

#Q7

def rmv(s):
    return s.replace("$", "")


#Q8

def even(l):
    even = []

    for i in l:
        if i % 2 == 0:
            even.append(i)

    return even


#Q9

def factorial():
    p = int(input("number: "))
    f = 1
    for i in range (1, p):
        f = f*i

    print("factorial: ", f )
    return f

#10


def div():
    div = []
    p = int(input("number: "))
    for i in range(1, p):
        if p % i == 0:
            div.append(i)

    print("divisors: ", div)
    return div


#Q11

def dist():
    xa = int(input("X value of point A: "))
    ya = int(input("Y value of point A: "))
    xb = int(input("X value of point B: "))
    yb = int(input("Y value of point B: "))

    g = ((xa - xb)**2 + (ya - yb)**2) ** 0.5

    return g

#Q12

def pt (m, n):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


