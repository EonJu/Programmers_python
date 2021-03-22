import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    chk = 0

    for i ,j in zip(progresses,speeds):
        n = float((100-i)/j)
        #소수점 남으면 올림처리
        n=math.ceil(n)
        if(len(q) == 0):
            q.append(n)
            continue
       
        chk = q.popleft()
        q.appendleft(chk)
        if(chk<n):
            print("chk!"+str(n))
            answer.append(len(q))
            q.clear()
            q.append(n)
        else:
            q.append(n)

    if(len(q)!=0):
        answer.append(len(q))
 
        
    
    print(answer)
    return answer


progresses =[96, 99, 98, 97]
speeds =[1,1,1,1]
solution(progresses, speeds)