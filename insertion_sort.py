import random

def insert_sorting(A):
    l=len(A)
    i=1
    while i<l:
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key
        i+=1
    return A



def merge_sorting(A,p,q,r):
    n_l=q-p+1
    n_r=r-q
    L=[]
    R=[]
    L[0:n_l]=A[p:q]
    R[0:n_r]=A[q:r]
    #set sentinel
    L.append(10**10)
    R.append(10**10)
    print L
    print R
    i=0
    j=0
    for k in range(p,r):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
    return A



#test insersion sort
#l_s=insert_sorting(l)
#print l_s


#test merge sort
l = []
for i in range(10):
    l.append(random.randint(0, 99))
for j in range(10):
    l.append(random.randint(0, 99))
#print l
l[0:10]=insert_sorting(l[0:10])
l[10:20]=insert_sorting(l[10:20])
print l
#get a sorting list l
l_merge=merge_sorting(l,2,10,20)
print l_merge