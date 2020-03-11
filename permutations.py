import math

print("If x points lie on a line, and y points lie on another parallel line, how many triangles can be formed by choosing three of these points?")

x = int(input("How many x points are there?: "))
y = int(input("How many y points are there?: "))

def nCr(n):
    f = math.factorial
    return f(n) / f(n-2) / f(2)

def per(x,y):
    return y*nCr(x) + x*nCr(y)  

print(int(per(x,y)))