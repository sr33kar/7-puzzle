import copy
print("White block=\'w\'\nBlack block=\'b\'\nEmpty block=\'_\'")
print("Enter the start configuration:")
s=input()
print("------------------------------")
cw=0
cb=0
ce=0
pe=0
l=0
for k in s:
    if k=='w':
        cw+=1
    if k=='b':
        cb+=1
    if k=='_':
        ce+=1
        pe=l
    l+=1
if cw!=3 or cb!=3 or ce!=1:
    print("Wrong input!!")
    exit()

def sorted(s):
    if s=="_wwwbbb" or s=="w_wwbbb" or s=="ww_wbbb" or s=="www_bbb" or s=="wwwb_bb" or s=="wwwbb_b" or s=="wwwbbb_":
        return True
    else:
        return False

visited=[]
stack=[]
s=list(s)
a=[]
stack.append([s,pe,0,a])  #string,index of _, cost, path list
#print(stack[0])
found=False
#while not found and sorted("".join(s)):
def insertIt(s,i,c,path):
    j=0
    if len(stack)==0:
        stack.append([s,i,c,path])
        return
    if s not in visited:
        stack.append([s,i,c,path])
finalCost=0
finalPath=[]
found=False
if sorted("".join(s)):
    finalCost=0
    finalPath=["".join(s)]
    found=True
while not found and len(stack)!=0:
    node=stack.pop(0)
    #print(node)
    ss=copy.deepcopy(node[0])
    i=node[1]
    cost=node[2]
    visited.append(ss)
    a=max(i-3,0)
    b=min(i+4,7)
    for j in range(a,b):
        path=copy.deepcopy(node[3])
        c=abs(j-i)
        if c==0:
            continue
        ss=copy.deepcopy(node[0])
        if c==1 or c==2:
            c=1
        if c==3:
            c=2
        temp=ss[i]
        #print(temp)
        ss[i]=ss[j]
        ss[j]=temp
        c+=cost
        path.append(ss)
        if sorted("".join(ss)):
            finalCost=c
            finalPath=copy.deepcopy(path)
            found=True
            break
        insertIt(ss,j,c,path)
print("Cost=",finalCost)
j=1
for i in finalPath:
    print("".join(i),j)
    j+=1





"""k=0
cost=0
i=pe

while not sorted(s):
    foundOne=False
    s=list(s)
    if k==0:
        ss=s[i+1:]
        k=1
        for j in range(len(ss)):
            if ss[j]=='w':
                s[i]='w'
                s[i+1+j]='_'
                i=i+1+j
                if j==0:
                    cost+=1
                else:
                    cost+=j
                foundOne=True
                break
    else:
        ss=s[:i]
        k=0
        l=len(ss)
        for j in range(len(ss)):
            if ss[l-j-1]=='b':
                s[i]='b'
                s[i-j-1]='_'
                i=i-j-1
                if j==0:
                    cost+=1
                else:
                    cost+=j
                foundOne=True
                break
    s="".join(s)
    if foundOne:
        print(s)
print("Cost:",cost)"""
