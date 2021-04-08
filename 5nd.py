array = list(map(int,input("숫자: ").split()))
commands = list(map(int,input("i, j, k: ").split()))

def solution(array, commands):                 #함수선언
    i = commands[0]
    j = commands[1]
    k = commands[2]
    
    array = array[i-1:j]                       #array 자르기
    array.sort()                               #잘라낸 array 정렬
    result = array[k-1]
    return result                              #결과값 return

print(solution(array, commands))