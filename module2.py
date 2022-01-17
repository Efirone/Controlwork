file=open('mat_dv.txt','r')
maxbal=dict()
L1=[]
winners=dict()
maxbalalg=dict()
alg=dict()
maxbalgeo=dict()
geo=dict()
for i in file:

    L=i.split()
    if L[2] not in maxbal:
        maxbal[L[2]] = int(L[3])+int(L[4])
        winners[L[2]] = str(int(L[3])+int(L[4])) +' '+L[0]+' '+L[1]
    elif(int(L[3])+int(L[4])>maxbal[L[2]]):
        maxbal[L[2]]= int(L[3])+int(L[4])
        winners[L[2]] = str(int(L[3])+int(L[4])) +' '+L[0]+' '+L[1]
    elif(int(L[3])+int(L[4])>maxbal[L[2]]):
        winners[L[2]] = winners[L[2]]+ str(int(L[3])+int(L[4])) +' '+L[0]+' '+L[1]


    if L[2] not in maxbalalg:
        maxbalalg[L[2]] = int(L[3])
        alg[L[2]] = str(int(L[3])) +' '+L[0]+' '+L[1]
    elif(int(L[3])>maxbalalg[L[2]]):
        maxbalalg[L[2]]= int(L[3])
        alg[L[2]] = str(int(L[3])) +' '+L[0]+' '+L[1]
    elif(int(L[3])==maxbalalg[L[2]]):
        alg[L[2]] = alg[L[2]]+ str(int(L[3])) +' '+L[0]+' '+L[1]

    if L[2] not in maxbalgeo:
        maxbalgeo[L[2]] = int(L[4])
        geo[L[2]] = str(int(L[4])) +' '+L[0]+' '+L[1]
    elif(int(L[4])>maxbalgeo[L[2]]):
        maxbalgeo[L[2]]= int(L[4])
        geo[L[2]] = str(int(L[4])) +' '+L[0]+' '+L[1]
    elif(int(L[4])==maxbalgeo[L[2]]):
        geo[L[2]] = geo[L[2]]+ str(int(L[4])) +' '+L[0]+' '+L[1]


file.close()
print(winners)
print(alg)
print(geo)




