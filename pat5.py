
'''
Pattern for :
            *           *
            * *       * *
            * * *   * * *
            * * * * * * *
'''

for i in range(1,5):
    for j in range(1,8):
        if(j<=i or j>7-i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
