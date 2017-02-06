def linearithmic(arr):
    for i in range(len(arr)):
        curr=arr[i]
        for j in range(1,len(arr)-i):
            if curr+arr[i+j]==8:
                return "Y",str(i),str(i+j)
    return "N"
