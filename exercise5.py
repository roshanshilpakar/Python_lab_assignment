s= input()
s=s.replace("","")
alpha_flag=[0]*26
for char in s:
    asci = ord(char)-97
    alpha_flag[asci]=1
asci=0
for i in range(0,len(alpha_flag)):
    if(alpha_flag[i]==0):
        asci=i+97
        print(char(asci),end="")