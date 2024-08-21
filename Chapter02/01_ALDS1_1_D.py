# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D&lang=ja

def main():
    N = int(input())
    R = [int(input()) for _ in range(N)]


    maxv = -10 ** 10    # 最大利益 maxv を十分小さい値で初期化
    minv = R[0]         # Rj の最小値

    for ri in R[1:]:
        maxv = max(maxv, ri - minv)     # 最大値を更新
        minv = min(minv, ri)            # 最小値を更新

    print(maxv)

if __name__ == '__main__':
    main()
