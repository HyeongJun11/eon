import math

N = int(input("몇 조각 : "))         # 몇 조각인지 입력
a = N//2                            # 입력 받은 수의 짝, 홀 구분하여 계산할 예정 
j=0
sum = 0

if N % 2 == 0:                       # 짝수일 경우
    for i in range(0, a+1):           
        b = int(math.factorial(a+i) / (math.factorial(a-i)*math.factorial(2*i)))    # 같은 요소를 포함하는 순열 구하는 공식을 미지수로 표현
        sum += b
else:                                # 홀수일 경우
    for i in range(1,N-a+1):
        b = int(math.factorial(a+i) / (math.factorial(a-j)*math.factorial(i+j)))    # 같은 요소를 포함하는 순열 구하는 공식을 미지수로 표현
        sum += b
        j = j+1

print(sum)