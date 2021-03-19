#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    
    maxidx = number.index(max(number)
    if(len(number) - maxidx >k):
        answer= number[maxide:]
    print(max(number))
    return answer


number = "4177252841"
k = 4

solution(number,k)