# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A&lang=jp

# 挿入ソート(0オリジン配列)
def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while (j >= 0 and A[j] > v):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print(*A)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(*A)
    insertionSort(A, N)

if __name__ == '__main__':
    main()
