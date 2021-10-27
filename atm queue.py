T=int(input(""))
for q in range(T):
    N,X=[int(x) for x in input().split()]
    Ai=list(map(int,input().split()))
    index=[x for x in range(1,N+1)]
    x=0
    o=0
    while len(Ai)<=0:
        if Ai[x]<=X:
            Ai.remove(Ai[x])
            o+=1
        elif Ai[x]>X:
            y=Ai[x]-X
            z=index[o]
            Ai.remove(Ai[x])
            Ai.append(y)
            index.remove(index[o])
            index.append(z)
    print("case#",q+1,":",*index)        

