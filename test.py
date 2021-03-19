"""
このファイルに解答コードを書いてください
"""
test_data = open('./input.txt', 'r')

# 行ごとにすべて読み込んでリストデータにする
inputs = test_data.readlines()


# # 入力受け取り
# inputs = []
# while True:
#     try:
#         _in = input()
#         inputs.append(_in)
    
#     except EOFError:
#         break

# mを取り出し
while True:
    try:
        m = int(inputs.pop())
        break
    except ValueError:
        continue
    
# 整形
ls = []
for inp in inputs:
    i, s = inp.split(':')
    i = int(i)
    s = s.replace('\n', '')

    ls.append([i, s])

# ソートと倍数の確認
ls = sorted(ls, key=lambda x: x[0])
ans = ''
for l in ls:
    i, s = l

    if m%i == 0:
        ans += s
    
# 出力
if ans == '':
    print(m)
else:
    print(ans)