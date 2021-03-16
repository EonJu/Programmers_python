def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        chk1 = str(bin(arr1[i]|arr2[i])[2:])
        chk1 ={:'0'>n}chk1
        chk1 = chk1.replace('1','#')
        chk1 = chk1.replace('0',' ')
        answer.append(chk1)       
    print(answer)   
    return answer

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
n = 6


solution(n,arr1,arr2)