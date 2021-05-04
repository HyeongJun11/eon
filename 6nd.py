import math

N = int(input("몇 조각 : "))         # 몇 조각인지 입력
a = N//2                            # 2로 나눴을 때 몫(입력 받은 수의 짝, 홀 구분하여 계산할 예정)
j=0
sum = 0

if N % 2 == 0:                       # 짝수일 경우
    for i in range(0, a+1):           
        b = int(math.factorial(a+i) / (math.factorial(a-i)*math.factorial(2*i)))    # N이 짝수일때 같은 요소가 있는 순열의 가지수를 미지수를 이용하여 공식화
        sum += b
else:                                # 홀수일 경우
    for i in range(1,N-a+1):
        b = int(math.factorial(a+i) / (math.factorial(a-j)*math.factorial(i+j)))    # N이 홀수일때 같은 요소가 있는 순열의 가지수를 미지수를 이용하여 공식화
        sum += b
        j += 1

print(sum)