"""
ID: baronli2
LANG: PYTHON3
TASK: ride
"""
def char2int(str):
    return ord(str)-ord('A')+1
import sys
sys.stdout=open("ride.out",'w')
sys.stdin=open("ride.in")
spaceship=input()
#print(ord(spaceship[0])-ord('A')+1)
a=1
for i in spaceship:
    a*=char2int(i)
a%=47
group=input()
#print(ord(spaceship[0])-ord('A')+1)
b=1
for i in group:
    b*=char2int(i)
b%=47
if a==b:
    print("GO")
else:
    print("STAY")    