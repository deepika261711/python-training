'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def leftover(a,b):
    left=""
    remove=set(b)
    for ch in a:
        if ch not in remove:
            left+=ch
    if left:
       print(left)
    else:
       print("empty")
A="ABCDEF"
B="BDE"
leftover(A,B)