
'''
Pattern for :
                   *
                  ***
                 *****
                *******
                 *****
                  ***
                   *
'''
k=1
for i in range(1,8):
    if(i>4):
        i=4-k
        k=k+1
    for j in range(1,8):
        if(4-i<j<4+i):
            print("*",end="")
        else:
            print(" ",end="")
    print()