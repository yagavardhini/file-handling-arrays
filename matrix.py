x=[[1,2,3],
[4,5,6],
[3,5,7]]
y=[[1,6,7],
   [4,7,9],
   [4,5,6]]
res= [[0,0,0],
      [0,0,0],
      [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j]=x[i][j]+y[i][j]
for r in res:
    print(r)
