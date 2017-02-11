def linear_pair(arr,sum_n):
    pair={}
    position={}
    for i in range(len(arr)):
        pair[arr[i]]=sum_n-int(arr[i])
        position[arr[i]]=i
        if pair[arr[i]] in pair:
            return 'Y', position[arr[i]], position[sum_n-arr[i]]
    return 'N'

array=[5,4,3,2,1,9,8,7]
print(linear_pair(array,20))
