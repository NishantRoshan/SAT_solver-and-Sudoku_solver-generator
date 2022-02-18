from sudoku import for_gen
import random
def cvr(rows,x,y,k,s):                   # function to check if number present at index (x,y) can be removed or not
    assumption=[]
    for i in range(2*k*k):
        for j in range(k*k):
            if(rows[i][j]!=0 and i!=x and j!=y):    # checking if the number at given index can be replaced by any other number or not
                assumption.append((int(i/(k*k)+1))*k**6+(i%(k*k))*k**4+j*k*k+rows[i][j])
    c1=rows[x][y]                                   #if the number at given index can be replaced by any other number, we would keep 
    for v in range(1,k*k+1):                        #it intact, else we will make it 0
        assumption.append((int(x/(k*k)+1))*k**6+(x%(k*k))*k**4+y*k*k+v)
        if(v==c1):
            del assumption[-1]
            continue
        if s.solve(assumptions=assumption):
            return False
        del assumption[-1]
    su[x][y]=c1
    return True
        
k=int(input("Put value of k : "))             #input is an integer k
s=for_gen(k)
su=[[k*k for j in range(k*k)] for i in range(2*k*k)]  #filling up the sudoku with numbers
s.solve()                                             #calling the solve function from prevoius question to fill the 
l=s.get_model()                                       #empty sudoku
l=[ele for ele in l if ele>0]
for ele in l:
    value=ele%(k*k)                                   #taking up the positive models and using the encoding to fill it3
    if value==0:
        value=k*k
    ele=int(ele/(k*k))
    j=ele%(k*k)
    ele=int(ele/(k*k))
    i=ele%(k*k)
    ele=int(ele/(k*k))
    s_n=ele
    su[i+(s_n-1)*k*k][j]=value               #finally the sudoku is filled with encodings
# print(su)
il=list(range(2*k*k))                         
jl=list(range(k*k))
random.shuffle(il)
random.shuffle(jl)
for i in il:
    for j in jl:
        if cvr(su,i,j,k,s):                 #one by one check if the numbers from filled sudoku can be removed
            # print("n")
            su[i][j]=0
print("S1:")                                #print sudoku 1
for i in range(k*k):
    for j in range(k*k):
        print(str(su[i][j])+" ",end="")
    print("")
print("S2:")                                #print sudoku 2
for i in range(k*k,2*k*k):
    for j in range(k*k):
        print(str(su[i][j])+" ",end="")
    print("")
