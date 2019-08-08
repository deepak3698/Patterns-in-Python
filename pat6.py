
'''
Pattern for : D
                * *
                *  *
                *   *
                *  *
                * *
'''
k=1
for i in range(1,6):
    if (i>3):
        i = 3 - k
        k = k + 1
    for j in range(1,5):
        if(j==1 or j==i+1):
            print("* ",end="")
        else:
            print(" ",end="")
    print()