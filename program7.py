def swap (A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
def rearrangeArray(A):
    for i in range(1,len(A),2):
        if A[i-1] > A[i]:
            swap(A,i-1,i)
A = [6,2,3,7,4,2]
rearrangeArray(A)
print(A)
