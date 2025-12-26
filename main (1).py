'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def cupcakes(n,arr):
    sum=0
    for i in range(n):
        if arr[i]>=5:
           sum+=arr[i]
    print(sum)
n=5
arr=[1,2,5,8,3,7]
cupcakes(n,arr)