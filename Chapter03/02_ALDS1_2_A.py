# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A&lang=ja

# バブルソート(0オリジン配列)
# 入替回数 sw を返す
def bubbleSort(A, N):
    flag = True
    i = 0
    sw = 0
    while flag:
        flag = False
        for j in range(N - 1, i, -1):
            if A[j - 1] > A[j]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
                sw += 1
        i += 1
    return sw

def main():
    N = int(input())
    A = list(map(int, input().split()))

    sw = bubbleSort(A, N)
    print(*A)
    print(sw)

if __name__ == '__main__':
    main()
