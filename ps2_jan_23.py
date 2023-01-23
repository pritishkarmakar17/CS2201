# Pritish Karmakar (21ms179)
# ps 3

#q1
L = [1,3,5,7]
for i in range(3):
    L.insert(2*i+1,2*(i+1))
    
print("output list is ",L)

#q2
L.pop()

print("modified list is", L)

#q3
def Push(List,e):
    return List.append(e)

List =[]
for i in range(5):
    Push(List,i+1)

print("output list :",List)

#q4
def Pop(List):
    return List.pop()
    
Pop(List)
print("output list :",List)

#q5
Names=[]
Push(Names,"Messi")
Push(Names,"Ronaldo")
Push(Names,"Mbappe")
Push(Names,"Neymar")
Push(Names,"Pritish")

for i in range(len(Names)):
    print(Pop(Names))

#q6
Str = "abcdcba"
lt=list(Str)
for i in range(len(lt)):
    print(Pop(lt), end='')

#q7
L = [1,2,1,2,5,6,2,5,6,8,4,3,8,6,4,8,7,4,6,8,6,1,4,5,6,5]
print("Output list is ",list(set(L)))

#q8
L=[1,2,3,4,5]
L1=[i for i in L if i%2==0]
print(L1)

#q9
L1=[1,2,3,4,5]
L2=[5,4,10,12]

L3=[i for L in [L1,L2] for i in L if i%2!=0]

print(L3)

#q10
while True:
    i=int(input("Enter an intiger: "))
    if i%2!=0:
        print("It\'s an odd number. EXIT")
        break
    else:
        print("It\'s an even number. CONTINUE")

#q11
z=int(input("Enter an intiger: "))

i=0
step=1

while True:
    i+=1
    k = z%(10**i)
    if k==z:
        break
    else:
        step+=1
        continue
        
rev=0
j=0
while j<step:
    rev+= (z%(10**(j+1))-z%(10**j))*10**(step-1-2*j)
    j+=1
    
print("reverse order:",int(rev))

#12
d={1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}

z=int(input("Enter an intiger: "))

i=0
step =1
while True:
    i+=1
    k = z%(10**i)
    if k==z:
        break
    else:
        step+=1
        continue


j=step
while j>0:
    num= (z%(10**(j))-z%(10**(j-1)))*10**(-j+1)
    #print(int(num))
    print(d[num], end=' ')
    j-=1

#13
from math import sin
import numpy as np

f = lambda x: sin(x)+x**2-1

xv=[]
a=0
b=1
step = 0.01
for i in np.arange(a,b,step):
    if f(i)*f(i+step)<0:
        xv.append((i,i+step))

print("better interval",xv)
sol=[]

print("\t x1\t\t x2\t\t x0\t\t f(x0)")

for i in xv:
    x1,x2=i[0],i[1]
    print("\n")
    
    k=0
    while True:
        # count
        k+=1
        # bisection point
        x0=(x1+x2)/2
        # if soln is in left part
        if f(x1)*f(x0)<0:
            x1=x1
            x2=x0
        # if soln is in right part    
        else:
            x1=x0
            x2=x2
        print("%i\t %.6f\t %.6f\t %.6f\t %.6f\t" %(k,x1,x2,x0,f(x0)))
        # required accuracy
        accuracy = 10**(-3)
        if abs(f(x0))<accuracy:
            sol.append(x0)
            break

print("\n")
if len(sol)==1:
    print(f"the solution:\t{sol[0]}")
elif len(sol)>1:
    print(f"no of solution in the range:\t{len(sol)}")
    print(f"the solutions:\t{sol}")
else:
    print("no solution in that range")

#q14
# define a function
f = lambda x: x**3 +x**2 -x

#initial guesses
x0=[-15,0,20]

#definr derivative
def dfdx(x):
    h=10e-4
    return (f(x+h)-f(x))/h

def h(x):
    return -f(x)/dfdx(x)
print("\tx\t\tf(x)")

k=0
while True:
    # count
    k+=1
    x0+=h(x0)
    print("%i\t%9.6f\t%9.6f"%(k,x0,f(x0)))
    if abs(f(x0))<10**(-3):
        sol = x0
        break

print("\n")
print(f"The solution: {sol}")




