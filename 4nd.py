x = list(map(int,input("숫자: ").split()))

def bubblesort(x):
    n= len(x)
    for i in range(0,n) :
        for j in range(n-1,i,-1):
            if x[j-1] > x[j]:
               x[j-1], x[j] = x[j], x[j-1]
    return x

print(bubblesort(x))