"""
ID: baronli2
LANG: PYTHON3
TASK: test
"""
import sys
sys.stdout=open("test.out",'w')
sys.stdin=open("test.in")
a,b=input().split()
print(eval(a+"+"+b))