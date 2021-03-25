x = list(map(int,input("숫자: ").split()))

def add(x):
    result = 0
    for i in x :
        result = result + i
    return result

print(add(x))