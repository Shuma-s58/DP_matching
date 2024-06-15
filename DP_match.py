import numpy as np
import math

sum = list(range(1, 101))

for i in range(100):
    sum[i] = f'{sum[i]:03}'

data_011 = []
datalist_011 = []
dataset_011 = []
for i in range(100):
  f = open('/mnt/d/city_mcedata/city011/city011_' + sum[i] + '.txt', 'r')
  datalist_011.append(f.readlines())
  dataset_011.append(datalist_011[i][3:])
  f.close()

data_012 = []
datalist_012 = []
dataset_012 = []
for i in range(100):
  f = open('/mnt/d/city_mcedata/city012/city012_' + sum[i] + '.txt', 'r')
  datalist_012.append(f.readlines())
  dataset_012.append(datalist_012[i][3:])
  f.close()

#2
dataset_AA = []
dataset_BB = []
for j in range(100):

    dataset_A = []
    for i in range(int(datalist_011[j][2])):
        dataset_A.append(dataset_011[j][i].split(" ")) # スペース区切りで配列化
        dataset_A[i] = [float(s) for s in dataset_A[i][:-1]] # "strからfloatへの変換" + "/n の消去 "

    dataset_B = []
    for i in range(int(datalist_012[j][2])):
        dataset_B.append(dataset_012[j][i].split(" ")) # スペース区切りで配列化
        dataset_B[i] = [float(s) for s in dataset_B[i][:-1]] # "strからfloatへの変換" + "/n の消去 "

    dataset_AA.append(dataset_A)
    dataset_BB.append(dataset_B)

#def1
# 局所距離の計算
def DISTANCE(A, B):
  distance_I = []
  for I in range(len(dataset_AA[A])):
    distance_J = []
    for J in range(len(dataset_BB[B])):

      all_A = 0 #0を定義したほうが正しい
      for k in range(len(dataset_AA[A][0])):
        all_A += (dataset_AA[A][I][k] - dataset_BB[B][J][k]) ** 2   # 2乗

      distance_J.append(all_A ** 0.5)    # √(all_A)
    distance_I.append(distance_J)

  return distance_I


#def2

def match(u):
  Tn = []
  for s in range(100):
    T = 0
    # 局所距離
    dis = DISTANCE(u, s) # u番目×s番目

    # 累積距離の定義
    g = [[0 for i in range(len(dis[0]))] for j in range(len(dis))]

    # 初期条件: 累積距離、局所距離
    g[0][0] = dis[0][0]

    # 累積距離を求める
    i = len(dis) - 1
    j = len(dis[0]) - 1

    # 境界条件
    for I in reversed(range(0, i)):
      g[i - I][j - j] = g[i - (I + 1)][j - j] + dis[i - I][j - j]
    for J in reversed(range(0, j)):
      g[i - i][j - J] = g[i - i][j - (J + 1)] + dis[i - i][j - J]

    # 累積距離
    for I in reversed(range(0, i)):
      for J in reversed(range(0, j)):
        g[i - I][j - J] = min(g[i - I][j - (J + 1)] + dis[i - I][j - J], g[i - (I + 1)][j - (J + 1)] + dis[i - I][j - J] * 2, g[i - (I + 1)][j - J] + dis[i - I][j - J])


    # 最終処理
    T = g[i][j] / (i + j)

    Tn.append(T)

  print(u + 1)
  print("Distance:", min(Tn))
  print("match:", Tn.index(min(Tn)) + 1)
  print("")

  if not Tn.index(min(Tn)) == u:
      print(u + 1, ":", Tn[u])
      print(Tn.index(min(Tn)) + 1, ":", Tn[Tn.index(min(Tn))])
      print(sorted(Tn))
      print("")

  return Tn.index(min(Tn))

#end

Tu = []
for u in range(100):
    if match(u) == u:
      Tu.append(u)

print("---")
print("end")
print((len(Tu) / 100) * 100, "%")
