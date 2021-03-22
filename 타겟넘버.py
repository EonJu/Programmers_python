answer =0

def dfs(index, numbers, sum, target):
    global answer
    n=len(numbers)
    #끝에 도달했으면
    if(index == n-1):
        #sum 값이 target값과 일치하면 answer++
        if(sum == target):
            answer+=1
    #끝이 아니라면
    else:   
        dfs(index+1 , numbers, sum+numbers[index+1],target)
        dfs(index+1 , numbers, sum-numbers[index+1],target)

def solution(numbers, target):
   
    dfs(-1,numbers,0,target)
    print(answer)
    return answer



numbers=[1, 1, 1, 1, 1]
target = 3
solution(numbers,target)
