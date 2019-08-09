

'''
Pattern for :
            A
            B B
            C C C
            D D D D
            E E E E E
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