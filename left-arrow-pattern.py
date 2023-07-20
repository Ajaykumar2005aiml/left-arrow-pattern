R=int(input()) #get input of rows
for i in range(1,R): #1 to R
    for j in range(1,i+1): #increamenting i one-by one
        if(i==R or j==i):#if condition for print only a star
            print("*",end="")
        else:#else for hallow spaces
            print(" ",end="")
    print()
#anothor code for decreasing pattern 
for i in range(1,R+1):
    for j in range(i,R+1):
        if(i==1 or j==R):
            print("*",end="")
        else:
            print(" ",end="")
    print()
