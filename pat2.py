
'''
Pattern for :
                ****
                ***
                **
                *
'''
print("######pattern(nxn)######")
n=int(input("Enter a number : "))
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end="")
    print()