'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def minion_game(string):
    k=0
    s=0
    v="AEIOU"
    for i in range(len(string)):
        if string[i] in v:
            k+=len(string)-i
        else:
            s+=len(string)-i
    if k>s:
                print("Kelvin",k)
    elif s>k:
                print("Stuart",s)
    else:
                print("Draw")
string="BANANA"
minion_game(string)