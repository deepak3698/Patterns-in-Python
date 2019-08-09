
'''
Pattern for :
                A
                B C
                D E F
                G H I J
                K L M N O

'''

print("######pattern(nxn)######")
n=int(input("Enter a number : "))
char=65
for i in range(0,n):
    for j in range(0,i+1):
        charr=chr(char)
        print(f"{charr}",end="")
        char=char+1
    print()