from typing import MappingView

n=str(input("enter a character:-"))
x=len(n)
m=n.upper()
p=list(m)
for i in range(x):
    if(p[i]=="A"):
        #alphabet "A"
        for row in range(6):
            for col in range(5):
                if ((col==0 or col==4) and row>=2) or row==3 or (row==0 and col==2) or (row==1 and (col==1 or col==3)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="B"):
        #alphabet "B"
        for row in range(5):
            for col in range(5):
                if(col==0 or (row%2==0 and col!=4) or (row%2!=0 and col==4)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="C"):
        #alphabet "C"
        for row in range(5):
            for col in range(5):
                if(col==0 or row==0 or row==4): 
                    print("*",end=" ")              
                else:
                    print(end="  ")
            print()
    if(p[i]=="D"):
        #alphabet "D"
        for row in range(5):
            for col in range(5):
                if(col==0 or ((row==0 or row==4) and col!=4) or (col==4 and (row>0 and row<4))):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="E"):
        #alphabet "E"
        for row in range(5):
            for col in range(5):
                if(col==0 or row==0 or row==4 or (row==2 and col<4)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="F"):
        #alphabet "F"
        for row in range(5):
            for col in range(5):
                if(col==0 or row==0 or (row==2 and col<4)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="G"):
        #alphabet "G"
        for row in range(5):
            for col in range(5):
                if((col==0 and (row>0 and row<4)) or (row==2 and col==3)or (row==4 and col==1) or row==0 or(row==4 and col%2==0) or (row ==3 and (col==2 or col==4))):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="H"):
        #alphabet "H"
        for row in range(5):
            for col in range(5):
                if(col==0 or col==4 or row==2):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="I"):
        #alphabet "I"
        for row in range(5):
            for col in range(5):
                if(row==0 or row==4 or col==2):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="J"):
        #alphabet "J"
        for row in range(5):
            for col in range(5):
                if(row==0 or (col==3 and row!=4) or (row==3 and col%2!=0) or (row==4 and col==2)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="K"):
        #alphabet "K"
        for row in range(5):
            for col in range(5):
                if(col==0 or (col==2 and row%2!=0)or (col==3 and (row%2==0 and row!=2))or (row==2 and col<2)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="L"):
        #alphabet "l"
        for row in range(5):
            for col in range(5):
                if(col==0 or row==4):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="M"):
        #alphabet "M"
        for row in range(5):
            for col in range(5):
                if(col==0 or col==4 or (row==1 and col%2!=0) or (row==2 and col==2)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="N"):
        #alphabet "N"
        for row in range(5):
            for col in range(5):
                if(col==0 or col==4 or row==col):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="O"):
        #alphabet "O"
        for row in range(5):
            for col in range(5):
                if((col==0 or col==4) and (row>0 and row<4)or(row==0 or row==4) and (col>0 and col<4)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="P"):
        #alphabet "P"
        for row in range(5):
            for col in range(5):
                if(col==0 or ((row==0 or row==2) and col!=4)or (row==1 and col==4)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="Q"):
        #alphabet "Q"
        for row in range(5):
            for col in range(5):
                if((col==0 or col==3) and (row>0 and row<3)or(row==0 or row==3) and (col>0 and col<3) or (row==col==4 )):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="R"):
        #alphabet "R"
        for row in range(5):
            for col in range(5):
                if(col==0 or ((row==0 or row==2) and col!=4)or (row==1 and col==4)or (row ==col and row==col!=1)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="S"):
        #alphabet "S"
        for row in range(5):
            for col in range(5):
                if((row==0 and col>0 )or (row==2 and (col>0 and col<4)) or (row==4 and col<4) or (col==0 and row==1)or (col==4 and row==3)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="T"):
        #alphabet "T"
        for row in range(5):
            for col in range(5):
                if(row==0 or col==2):
                     print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="U"):
        #alphabet "U"
        for row in range(5):
            for col in range(5):
                if((col==0 and row!=4) or (col==4 and row!=4) or (row==4 and (col>0 and col<4))):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="V"):
        #alphabet "V"
        for row in range(5):
            for col in range(5):
                if((row==4 and col==2) or((col==0 or col==4) and row<3)or (row==3 and col%2!=0)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="W"):
        #alphabet "W"
        for row in range(5):
            for col in range(5):
                if((col==0 or col==4)or (row==3 and col%2!=0)or row==col==2):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="X"):
        #alphabet "X"
        for row in range(5):
            for col in range(5):
                if(row==col or (row==0 and col==4) or (row ==1 and col==3) or (row ==4 and col==0) or (row ==3 and col==1)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="Y"):
        #alphabet "Y"
        for row in range(5):
            for col in range(5):
                if(((row==col and row<3 )and col<3)or (col==2 and row>2)or (row==0 and col==4) or (row ==1 and col==3)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
    if(p[i]=="Z"):
        #alphabet "Z"
        for row in range(5):
            for col in range(5):
                if(row==0 or row==4 or (row==1 and col==3)or (row==2 and col==2)or (row==3 and col==1)):
                    print("*",end=" ")
                else:
                    print(end="  ")
            print()
        if(p[i]=="*"):
            #alphabet "*"
            for row in range(5):
                for col in range(5):
                    if(row==col or (row==0 and col==4) or (row ==1 and col==3) or (row ==4 and col==0) or (row ==3 and col==1)):
                        print("*",end=" ")
                    else:
                        print(end="  ")
                print()
print("\n")
print("\n")
    

