def removeThirdNumber(list):
    temp=[]
    p=1
    s=0
    for i in range(0,len(list)):
        s=(p+s)%len(list)
        el = list.pop(s)
        temp.append(el)
    return temp
    
n=int(input())
list=[]
for i in range(0,n):
    list.append(int(input()))
p=removeThirdNumber(list)
print(p)