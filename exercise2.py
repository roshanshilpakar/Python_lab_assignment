def countX(lst,x):
    count=0
    for ele in lst:
        if ele==x:
            count = count+1
        print(count)
        
lst=[]
n= int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    
x= int(input())
countX(lst,x)