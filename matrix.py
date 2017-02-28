import random
def generate_matrix(m,n):
    final_matrix=[]
    for row in range(m):
        final_matrix.append([])
        for column in range(n):
            random_number=random.randint(1,m*n)
            final_matrix[row].append(random_number)
            print(random_number,end=' ')
        print()
    return final_matrix
def product_matrix(A,B):
    if len(A[0])==len(B):
        A,B=B,A
    if len(A)==len(B[0]):
        if len(A[0])==len(B) and len(A)<len(A[0]):
            A,B=B,A
        for row in range(len(A)):
            for column in range(len(B[0])):
                curr_product=0
                for curr_pos in range(len(A[0])):
                    curr_product+=A[row][curr_pos]*B[curr_pos][column]
                print("{:5}".format(curr_product),end='')
            print()
    else:
        print('NA')
def sum_matrix(A,B):
    if A==[] or B==[]:
        return
    if len(A)==len(B) and len(A[0])==len(B[0]):
        for column in range(len(A[0])):
            curr_sum=A[0][column]+B[0][column]
            print("{:3}".format(curr_sum),end='')
        print()
        return(sum_matrix(A[1:],B[1:]))
    else:
        print('NA')

m=[0,0]
n=[0,0]
done=False
while True:
    for matrixes in range(1,3):
        print("Matrix "+str(matrixes))
        while True:
            try:
                m[matrixes-1]=int(input("Enter m: "))
                if m[matrixes-1]==-1:
                    break
                if m[matrixes-1]<1 or m[matrixes-1]>5:
                    continue
                break
            except Exception as e:
                continue
        while True:
            try:
                n[matrixes-1]=int(input("Enter n: "))
                if n[matrixes-1]==-1:
                    break
                if n[matrixes-1]<1 or n[matrixes-1]>5:
                    continue
                break
            except Exception as e:
                continue
        if m[matrixes-1]==-1 and n[matrixes-1]==-1:
            done=True
            break
    if done == True:
        print("Bye")
        break
    print("Matrix 1")
    matrix1=generate_matrix(m[0],n[0])
    print("Matrix 2")
    matrix2=generate_matrix(m[1],n[1])
    print("Sum")
    sum_matrix(matrix1,matrix2)
    print("Product")
    product_matrix(matrix1,matrix2)
