def linearithmic(arr,sum_n):
    for i in range(len(arr)):
        curr=arr[i]
        for j in range(1,len(arr)-i):
            if curr+arr[i+j]==sum_n:
                return "Y",str(i),str(i+j)
    return "N"
