'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

x=int(input("Enter a number:"))
for i in range(1,x+1):
    if (i%3==0) and (i%5==0):
        print("fizzbuzz")
    
    elif i%3==0:
         print("fizz")
    elif i%5==0:
         print("buzz")
    
    else:
         print(i)