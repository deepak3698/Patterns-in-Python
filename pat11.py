
'''
Pattern for :
                A
                A B
                A B C
                A B C D
                A B C D E

'''

print("######pattern(nxn)######")
n=int(input("Enter a number : "))
char=65
for i in range(0,n):
    for j in range(0,i+1):
        charr=chr(char)
        print(f"{charr} ",end="")
        char=char+1
    char=65
    print()