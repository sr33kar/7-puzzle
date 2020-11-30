"""
assume
heuristic: h(s)=number of 'w's after first b + number of 'b's before last w
in the previous code, now instead of alternative choosing of what to swap, i'll swap with nearest 'w' and 'b' and depending on h(s) s will be assigned
if h(s)=0 the stop

wwbwbb_

"""
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

def h(s):
    cB=0
    cW=0
    nB=0
    nW=0
    for i in s:
        if i=='w':
            cW+=1
            if cB!=0:
                nW+=1
        if i=='b':
            cB+=1
            if cW<3:
                nB+=1
    return nB+nW

visited=[]
stack=[]
s=list(s)
#print(h(s))
#print(h("w_wbwbb"))
#print(h("ww_bwbb"))
a=[]
stack.append([s,pe,0,a,0])  #string,index of _, cost, path list
#print(stack[0])
found=False

#while not found and sorted("".join(s)):
def insertIt(s,i,c,path,ch):
    j=0
    cAndH=c+h(s)+ch
    if len(stack)==0:
        stack.append([s,i,c,path,cAndH])
        return
    if s not in visited:
        while cAndH>stack[j][4]:
            j+=1
            if j==len(stack):
                stack.append([s,i,c,path,cAndH])
                return
        stack.insert(j,[s,i,c,path,cAndH])
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
    #print(a,b)
    ch=node[4]
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
        insertIt(ss,j,c,path,ch)
print("Cost=",finalCost)
j=1
for i in finalPath:
    print("".join(i),j)
    j+=1



"""
print(h(s))
k=0
cost=0
i=pe

while True:
    foundOne=False
    s=list(s)
    s1=s
    s2=s
    ss=s[i+1:]
    k=1
    temp=i
    c1=0
    c2=0
    for j in range(len(ss)):
        if ss[j]=='w':
            s1[temp]='w'
            s1[temp+1+j]='_'
            temp=temp+1+j
            if j==0:
                c1+=1
            else:
                c1+=j
            foundOne=True
            break
    ss=s[:i]
    k=0
    t2=i
    l=len(ss)
    for j in range(len(ss)):
        if ss[l-j-1]=='b':
            s2[t2]='b'
            s2[t2-j-1]='_'
            t2=t2-j-1
            if j==0:
                c2+=1
            else:
                c2+=j
            foundOne=True
            break
    if h(s1)>h(s2):
        i=t2
        s=s2
        if h(s2)==0:
            break
    else:
        i=temp
        s=s1
        if h(s1)==0:
            break

    s="".join(s)
    print(s)
print(h(s))
print("Cost:",cost)"""
