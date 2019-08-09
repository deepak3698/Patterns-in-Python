

'''
Pattern for :
            1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5
'''

print("######pattern(nxn)######")
n=int(input("Enter a number : "))
for i in range(0,n):
    for j in range(0,i+1):
        print(f"{j+1}",end="")
        j=j+1
    print()
