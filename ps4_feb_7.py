# Pritish karmakar (21ms179)
# problem set 4

import numpy as np

#1
l1=[1,2,3,4]
l2=[1,3,7,9]

l_out=[i for i in l1 if i not in l2]
print(l_out)

#2
vol_cyl= lambda r,h: np.pi*h*r**2

R= float(input('Enter the radius: '))
H= float(input('Enter the height: '))

print('volume of the cylinder:',vol_cyl(R,H))

#3
name= str(input('Enter employee name: '))
B= int(input('Enter basic salary: '))

DA = 0.17*B
HRA=0.08*B
MA=0.1*B
T = DA + HRA + MA

l= len(name)

print(f"%-{l+3}s%-16s"%("+"+"-"*(l+2),"+--------------+" ))
print(f"%-{l+3}s%-15s"%("| NAME","| TOTAL SALARY |" ))
print(f"%-{l+3}s%-16s"%("+"+"-"*(l+2),"+--------------+" ))
print(f"| %-{l}s | %12.3f |"%(name,T))
print(f"%-{l+3}s%-16s"%("+"+"-"*(l+2),"+--------------+" ))

print(f'The salary of {name} is {T}.')

#4
print('The salary of {0:7s} is: {1:12.3f}'.format(name,T))

#5
print(np.arange(1,2.5,0.5))
print(np.arange(1,3.5,0.5))
print(np.arange(1,4.5,0.5))

#6







