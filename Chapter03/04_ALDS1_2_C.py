# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C&lang=jp

import copy

def bubbleSort(A, N):
    for i in range(N - 1):
        for j in range(N - 1, i, -1):
            if int(A[j][1]) < int(A[j - 1][1]):
                A[j], A[j - 1] = A[j - 1], A[j]

def selectionSort(A, N):
    for i in range(N - 1):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i], A[minj] = A[minj], A[i]

def isStable(C1, C2, N):
    for i in range(N):
        if C1[i] != C2[i]:
            return False
    return True

def main():
    N = int(input())
    C1 = list(input().split())
    C2 = copy.deepcopy(C1)

    bubbleSort(C1, N)
    print(*C1)
    print("Stable")

    selectionSort(C2, N)
    print(*C2)
    if isStable(C1, C2, N):
        print("Stable")
    else:
        print("Not stable")

if __name__ == '__main__':
    main()
