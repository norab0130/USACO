"""
ID: baronli2
LANG: PYTHON3
TASK: gift1
"""
import sys
sys.stdout=open("gift1.out",'w')
sys.stdin=open("gift1.in")
name=eval(input())
names={}
for i in range(name):
    names[input()]=0
for i in range(name):
    giver=input()
    given_mon,given_persons=input().split()
    if given_mon==2000:
        pass
    given_mon=eval(given_mon)
    given_persons=eval(given_persons)
    names[giver]-=given_mon
    if given_persons==0 or given_mon%given_persons==0:
        for i in range(given_persons):
            names[input()]+=given_mon/given_persons
    elif given_mon%given_persons!=0:
        names[giver]+=given_mon%given_persons
        given_mon-=given_mon%given_persons
        for i in range(given_persons):
            names[input()]+=given_mon/given_persons
for i in names.items():
    print(str(i[0])+" "+str(int(i[1])))