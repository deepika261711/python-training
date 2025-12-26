'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def check(x):
    l=0
    r=len(x)-1
    while l<r:
     if x[l]!=x[r]:
        return "not a palindrome"
     else:
                l+=1
                r-=1
    return "palindrome"
x="madam"
print(check(x))