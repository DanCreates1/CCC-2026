S1 = int(input())
S2 = int(input())
S3 = int(input())
S4 = int(input())
S5 = int(input())
arr = [S1, S2, S3, S4, S5]

D = int(input()) # event’s difficulty factor

arr.sort()

arr.remove(arr[-1])
arr.remove(arr[0])


count = 0
i = 0

while i < 3:
    count = count + int(arr[i])
    i=i+1
    

FinalResult = count * D
print(FinalResult)

