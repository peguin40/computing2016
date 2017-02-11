def quadratic(arr,sum_n):
    for i in range(len(arr)):
        curr=arr[i]
        for j in range(len(arr)):
            if i==j:
                pass
            elif curr+arr[j]==sum_n:
                return "Y",str(i),str(j)
    return "N"
