import csv
from pysat.solvers import Solver
from pysat.card import *
import math
import time

def for_gen(k):  #generates the formula for the solver
    cnf=CNF()    #
    s=Solver(name='m22')  #Take MiniSat22 Solver

# the encoding for each element in sudoku-1/sudoku-2, row 'i', column 'j' and value 'v' is described as follows:
# (1 (if element is in sudoku-1) / 2 (otherwise))*k^6 + i*k^4 + j*k^2 + v

    for i in range(k*k):   #ensures that the value in each cell of the first-sudoku is between 1 to k*k  
        for j in range(k*k):
            s.add_clause([1*k**6+i*k**4+j*k*k+v for v in range(1,k*k+1)])

    for i in range(k*k,2*k*k):  #ensures that the value in each cell of the second-sudoku is between 1 to k*k 
        for j in range(k*k):
            s.add_clause([2*k**6+(i-k*k)*k**4+j*k*k+v for v in range(1,k*k+1)])

    for i in range(k*k):    #ensures that no two elements in a row 'i' of the first-sudoku are same
        for x in range(k*k): 
            for y in range(x+1,k*k):    #take two different cells of row 'i' with column-index 'x' and 'y'
                for v in range(1,k*k+1):
                    s.add_clause([-(1*k**6 + i*k**4 + x*k*k + v),-(1*k**6 + i*k**4 + y*k*k + v)])

    for i in range(k*k,2*k*k): #ensures that no two elements in a row 'i' of the second-sudoku are same
        for x in range(k*k):
            for y in range(x+1,k*k):  
                for v in range(1,k*k+1):
                    s.add_clause([-(2*k**6 + (i-k*k)*k**4 + x*k*k + v),-(2*k**6 + (i-k*k)*k**4 + y*k*k + v)])

    for j in range(k*k):    #ensures that no two elements in a column 'j' of first-sudoku are same
        for x in range(k*k):
            for y in range(x+1,k*k):      #take two different cells of column 'j' with row-index 'x' and 'y'
                for v in range(1,k*k+1):
                    s.add_clause([-(1*k**6 + x*k**4 + j*k*k + v),-(1*k**6 + y*k**4 + j*k*k + v)])

    for j in range(k*k): #ensures that no two elements in a column 'j' of second-sudoku are same
        for x in range(k*k,2*k*k):
            for y in range(x+1,2*k*k):
                for v in range(1,k*k+1):
                    s.add_clause([-(2*k**6 + (x-k*k)*k**4 + j*k*k + v),-(2*k**6 + (y-k*k)*k**4 + j*k*k + v)])

    for i in range(k):   #In first-sudoku, it ensures that no two elements in a grid are same and grid contains all the elements from 1 to k^2
        for j in range(k):    #select the grid
            for v in range(1,k*k+1): #select the value whose cardinality must be '1'   
                sudoku1=[]
                for x in range(i*k,(i+1)*k):     #iterate through the selected grid
                    for y in range(j*k,(j+1)*k):
                        sudoku1.append(1*k**6+x*k**4+y*k*k+v)
                cnf.extend(CardEnc.equals(lits=sudoku1,bound=1,encoding=0))

    for i in range(k):    #In second-sudoku, it ensures that no two elements in a grid are same and grid contains all the elements from 1 to k^2
        for j in range(k):
            for v in range(1,k*k+1):
                sudoku2=[]
                for x in range((i+k)*k,(i+1+k)*k):
                    for y in range(j*k,(j+1)*k):
                        sudoku2.append(2*k**6+(x-k*k)*k**4+y*k*k+v)
                cnf.extend(CardEnc.equals(lits=sudoku2,bound=1,encoding=0))

    for i in range(k*k):   # it ensures that no two corresponding elements are same in first-sudoku and second-sudoku
        for j in range(k*k):  # select two corresponding cells of first sudoku and second sudoku
            for v in range(1,k*k+1):   #select a value 
                s.add_clause([-(1*k**6+i*k**4+j*k*k+v),-(2*k**6+i*k**4+j*k*k+v)])
    s.append_formula(cnf.clauses)
    return s

if __name__=="__main__":        
    filename="mycsv.csv"   #import csv file
    rows=[]                #list for sudoku
    with open(filename,'r') as csvfile: 
        csvreader = csv.reader(csvfile)  #read csv file
        for row in csvreader:         #take a row of csv
            roewi=[]                  #new 1-D list
            for e in row:             #any element in row
                roewi.append(int(e))  #convert that element into integer 
            rows.append(roewi)        #update the rows list
    k1=(len(rows))/2                  
    k=int(math.sqrt(k1))              # calculate k
    s=for_gen(k)                      #call formula generator function
    assumption=[]                     # a new list for assumptions(the values which are already given in the partially-filled sudoku)
    for i in range(k*k):              # assumptions in the first-sudoku
        for j in range(k*k):          
            if(rows[i][j]!=0):        #the element is provided to us
                assumption.append(1*k**6+i*k**4+j*k*k+rows[i][j])  # encode it in our formula
    for i in range(k*k,2*k*k):   # assumptions in the second-sudoku
        for j in range(k*k):
            if(rows[i][j]!=0):
                assumption.append(2*k**6+(i-k*k)*k**4+j*k*k+rows[i][j])
    start_time=time.time()           
    result=s.solve(assumptions=assumption)
    end_time=time.time()
    if result:
        model=s.get_model()       
        model=[ele for ele in model if ele>=0]                # we will take all elements which are non-negative in the model 
        s1=[[k*k for i in range(k*k)] for i in range(k*k)]    # 2-D list creation for first-sudoku
        s2=[[k*k for i in range(k*k)] for i in range(k*k)]    # 2-D list creation for second-sudoku
        for ele in model:                 
            value=ele%(k*k)           # get v from encoding                
            if value==0:              # (k^2 % k^2) is 0                 
               value=k*k
            ele=int(ele/(k*k))        # now get the column number 
            j=ele%(k*k)
            ele=int(ele/(k*k))        # now get the row number
            i=ele%(k*k)
            ele=int(ele/(k*k))        # now get the sudoku in which the element is present
            s_n=ele
            if(s_n==1):     
                s1[i][j]=value
            else:
                s2[i][j]=value
        s.delete()
        print("S1")        # print(sudoku-1)
        for i in s1:      
            for j in i:    
                print(str(j)+" ",end="")
            print("")
        print("S2")
        for i in s2:
            for j in i:
                print(str(j)+" ",end="")
            print("")
    else:
        s.delete()
        print("None")