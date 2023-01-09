# problem set 1
# Pritish Karmakar (21MS179)

# Q1 (a)
x= [x for x in range(0,10)]

#Q1 (b)
y= [x for x in range(3,12)]

#Q1 (c)
print(x[-1::-1])

#Q1 (d)
print(f"odd entries are {x[1::2]} and even entries are {x[0::2]}")

#Q1 (e)
if x[3]==y[0]:
    print("they are same")
else:
    print("not same")

#Q1 (f)
if 10 in x:
    print("index is ",x.index(10))
else:
    print("not there")

#Q1 (g)
if 7 in x:
    print("index is ",y.index(7))
else:
    print("not there")

#Q1 (h)
l1 = x+y

#Q1 (i)
print(f"location of max is {l1.index(max(l1))} and location of min is {l1.index(min(l1))}.")

#Q2 (a)
x = "The quick brown fox jumps over the lazy dog"

#Q2 (b)
print("output is ",list(x)[0::3])

#Q2 (c)
print("reverse output is ", ''.join(list(x)[-1::-1]))

#Q2 (d)
print("output is ",list(x)[0::4])

#Q2 (e)
if "fox" in x:
    print("it is there")
else:
    print("it is not there")

#Q2 (f)
print("no of charecter is ",len(list(x)))

#Q2 (g)
print("output is ",list(x)[-1::-2])

#Q2 (h)
y = list(x)[0:4]
z = list(x)[-1:-4]

print("output is ",y+z)

#Q2 (i)
print("output is ", y*10 )

#Q3 (a)
print("hello world")

#Q3 (b)
# printing Hello, World
print("hello World")

#Q3 (c)
name = "Pritish"
age = 21
roll = "21MS179"

print(f"Hello! My name is {name}. i am {age} years old. My roll number is {roll}")
#Q3 (d)
x=[]
for i in range(0,2):
    a = str(input(f"enter number string {i+1}: "))
    x.append(float(a))

print("the sum is ", sum(x))

#Q3 (e)
x=[]
for i in range(0,2):
    a = int(input(f"enter intiger {i+1}: "))
    x.append(a)

print("the sum is ", sum(x))

#Q3 (f)
print("It\'s good to learn Python")

#Q3 (g)
print("The man asked, \"Where to meet you?\" I said, \"Well, use Google Meet!\"")

#Q3 (h)
l3=[]
i = int(input("enter a intiger: "))
l3.append(i)
f = float(input("enter a float: "))
l3.append(f)
s = str(input("enter a charecter: "))
l3.append(s)

for x in l3:
    print(f"{x} is",type(x))

#Q3 (i)
name=str(input("enter your name: "))
print("my name is {}".format(name))

print("my name is %s"%(name))

