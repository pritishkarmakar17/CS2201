# problem set 2
# Pritish Karmakar (21ms179)

#1
strg = 'abcdefghijkl'
l=0
while True:
    print(strg[l:])
    l+=1
    if l==len(strg):
        break

#2 
lt = [1,5,12,3,2,14,54,12,23,6,44]
l0 = lt[0]

for i in range(len(lt)):
    if l0<=lt[i]:
        l0=lt[i]
print('max number is ',l0)

#3
name = str(input("enter your name: "))
lt = list(name)
abb = [lt[0].upper()]
for i in range(len(lt)):
    if lt[i]==' ':
        abb.append(lt[i+1].upper())

print('Abbreviaton of your name:',''.join(abb))

#4
l= int(input("length of fibonacci seq required: "))
f=[1,1]
for i in range(2,l):
    fv= f[i-2]+f[i-1]
    f.append(fv)
print(f)

#5
n = int(input("no of line required: "))
lt3 = [str(i)+' ' for i in range(1,n+1)]

for i in range(n):
    print(''.join(lt3[:i+1]))

#6
n = int(input("no of line required: "))
lt3 = [str(2*i-1)+' ' for i in range(1,n+1)]

for i in range(n):
    print(''.join(lt3[:i+1]),'\n')

#7
n = int(input("no of line required: "))
lt3 = [str(i)+' ' for i in range(1,n+1)]

for i in range(n):
    print(''.join(lt3[:len(lt3)-i]))

#8
n = int(input("no of line required: "))
lt4 = [str(i)+' ' for i in range(1,n+1)]
lt5 = lt4 + lt4[-2::-1]

for i in range(n):
    print('  '*i,''.join(lt5[i:len(lt5)-i]))

#9
dt={'pritish':'12345', 'pradeep':'56789'}
userid = str(input("Your User ID: "))
if userid in dt.keys():
    passwd = str(input("Your password: "))
    if passwd==dt[userid]:
        print('Welcome to Welearn portal!')
    else:
        print('Invalid credentials!')
else:
    print("Invalid Username")
    
answ = str(input("Want to change password [y/n]: "))
if answ == 'y':
    userid = str(input("Your User ID: "))
    if userid in dt.keys():
        passwd = str(input("Your password: "))
        if passwd==dt[userid]:
            
            while True:
                new_pw=[passwd,passwd]
                for i in range(2):
                    pw = str(input("New password: "))
                    new_pw[i]=pw
                if new_pw[0]==new_pw[1]:
                    dt[userid]=new_pw[0]
                    break
                else:
                    print("new password not matched")
                    ans = str(input("Wanna try again [y/n]: "))
                    if ans=='y':
                        continue
                    else:
                        break
        else:
            print('Invalid credentials!')
    else:
        print("Invalid Username")

print("updated dict: ",dt)

#10
from math import *
import numpy as np

f = lambda x: sin(x) + x**2 -1

xv=[]
for i in np.arange(0,1.1,.1):
    if f(i)*f(i+0.1)<0:
        xv.append((i,i+1))
sol=[]

for i in xv:
    
    x1,x2=i[0],i[1]
    while True:
        x0=(x1+x2)/2

        if f(x1)*f(x0)<0:
            x1=x1
            x2=x0
        else:
            x1=x0
            x2=x2
        if abs(f(x0))<10**(-3):
            sol.append(x0)
            break

print(f"no of solution in the range: {len(sol)}")
if len(sol)>0:
    print(f"the solution: {sol}")

