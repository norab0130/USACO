"""
ID: baronli2
LANG: PYTHON3
TASK: friday
"""
import sys
sys.stdout=open("friday.out",'w')
sys.stdin=open("friday.in")
n=eval(input())
def a(str):
    if (n+1900)
leap_year=False
c=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
d=0
for i in range(n):
    if (n+1900)%4==0:
        if (n+1900)%100==0:
            if (n+1900)%400==0:
                x=(i*366)%7
            x=(i*365)%7
        x=(i*365)%7
    x=(i*365)%7
    r=1
    y=1
    if x==0:
        if y==13:
            c7+=1
        y+=1
    if x==1:
        if y==13:
            c+=1
        y+=1
    if x==2:
        if y==13:
            c2+=1
        y+=1
    if x==3:
        if y==13:
            c3+=1
        y+=1
    if x==4:
        if y==13:
            c4+=1
        y+=1
    if x==5:
        if y==13:
            c5+=1
        y+=1
    if x==6:
        if y==13:
            c6+=1
        y+=1
    if r==1 or r==3 or r==5 or r==7 or r==9 or r==11:
        if y>31:
            y=1
    elif r!=2:
        if y>30:
            y=1
    else:
        if leap_year==False:
            if y>28:
                y=1
        if leap_year==True:
            if y>29:
                y=1
print(str(c6)+" "+str(c7)+" "+str(c)+" "+str(c2)+" "+str(c3)+" "+str(c4)+" "+str(c5))