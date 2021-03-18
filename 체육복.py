#풀이 2
def solution(n, lost, reserve):
    chkreserve = [r for r in reserve if r not in lost]
    chklost = [l for l in lost if l not in reserve]

    for r in chkreserve:
        left = r-1
        right = r+1

        if left in chklost:
            chklost.remove(left)
        
        elif right in chklost:
            chklost.remove(right)

    return n-len(chklost)



#풀이 1 노가다 풀이
def solution1(n, lost, reserve):
    answer = 0
    arr = [1]*n;

    for j in range(n):
        #옷 갯수 넣어주기
        if j+1 in lost:
            arr[j] -=1
        if j+1 in reserve:
            arr[j] +=1
    for i in range(n):    
        if( arr[i]== 0 ):
            if(0<i<n-1):
                #왼쪽
                if(arr[i-1] == 2):
                    arr[i-1] -= 1
                    arr[i] +=1
                #오른쪽
                elif(arr[i+1] == 2):
                    arr[i+1] -=1
                    arr[i] +=1

            elif(i == 0):
                #오른쪽만
                if(arr[i+1] == 2):
                    arr[i+1] -=1
                    arr[i] +=1
            else:
                #왼쪽만
                if(arr[i-1] == 2):
                    arr[i-1] -= 1
                    arr[i] +=1

    print(arr)
    print(n- arr.count(0))

    return n-arr.count(0)

n=9
lost =[2,4,7,8]
reserve = [3,6,9]

solution(n, lost, reserve)