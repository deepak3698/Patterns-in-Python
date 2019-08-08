
'''
Pattern for :
               *
              ***
             *****
            *******
'''
for i in range(1,5):
    for j in range(1,8):
        if(4-i<j<4+i):
            print("*",end="")
        else:
            print(" ",end="")
    print()