def solution(board, moves):
    answer = 0
    arr=[]
    print("Test")
    for i in moves:
        for j in range(len(board)):
            if(board[j][i-1] == 0):
                pass
            else:
                arr.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if(len(arr)>=2 and arr[-1]==arr[-2]):
            answer+=2
            arr.pop(-1)
            arr.pop(-1)

    print(answer)
    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves =[1,5,3,5,1,2,1,4]
solution(board,moves) 