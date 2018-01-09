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

l=[]
for i in range(20):
    l.append(random.randint(0,99))

l_s=insert_sorting(l)
print l_s