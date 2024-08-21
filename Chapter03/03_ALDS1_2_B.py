# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B&lang=jp

N = int(input())
A = list(map(int, input().split()))

# 選択ソート
def selectionSort(A, N):
    # 交換回数
    sw = 0
    for i in range(N - 1):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            sw += 1
            A[i], A[minj] = A[minj], A[i]
    
    return sw

def main():
    sw = selectionSort(A, N)
    print(*A)
    print(sw)

if __name__ == '__main__':
    main()
