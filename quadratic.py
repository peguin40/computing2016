def quadratic(arr):
    for i in range(len(arr)):
        curr=arr[i]
        for j in range(len(arr)):
            if i==j:
                pass
            elif curr+arr[j]==8:
                return "Y",str(i),str(j)
    return "N"
