n = int(input())
goods = [list(map(int, input().split())) for _ in range(n)]
W = int(input())

# dp = [[0]*(W+1)]*(n+1)　この書き方はあまりお勧めされない
dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

# dpを考える
# 求めたいのはdp[n][W]
# dp[i][w] : i個の品物から重さがwを超えないように選んだときの、
#            価値の総和の最大値
# i = 0,..,n  w = 0,..,W
# dp[0][w](w=0,..,W) : 何も選ばないとき
# dp[1][w](w=0,..,W) : 一つ目までの品物で重さがwを超えないように選んだときの
#                      価値の総和の最大値
# ...
# dp[i+1][w](w=0,..,W) : i+1番目の品物で重さがwを超えないように選んだときの
#                        価値の総和の最大値
# 漸化式を作る
# 品物を選ぶ場合 ：
# 上限からその品物の重さを引いた重さを上限としたときの最大値に価値を加える
# dp[i+1][w] = dp[i][w-weight] + value (w>=weightの時のみ)
# 選ばない場合：
# i番目まで見たときと同じ値
# dp[i+1][w] = dp[i][w]
# 品物を選ぶ場合と選ばない場合の価値の総和が大きい方を選択！

for i, item in enumerate(goods):
    weight = item[0]
    value = item[1]
    for w in range(W+1):
        if w < weight:
            dp[i+1][w] = dp[i][w]
        else:
            # 選ぶ場合
            select = dp[i][w-weight] + value
            # 選ばない場合
            noSelect = dp[i][w]
            # 大きい方をとる
            dp[i+1][w] = max(select, noSelect)

print(dp[n][W])
