#https://programmers.co.kr/learn/courses/30/lessons/43162



def dfs(computers,n,start,visited):
    visited[start] = True

    for i in range(n):
        if(computers[start][i]==1 and i != start and visited[i] == False):
            dfs(computers,n,i,visited)
                
            

def solution(n, computers):
    answer = 0
    visited = [False] *n
   
    for i in range(n):
        if(visited[i]==True):
            continue
        answer+=1
        dfs(computers,n,i,visited)
    print(answer)
    return answer




n = 4
computers =  [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
solution(n,computers)