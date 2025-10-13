f1=open("acids.txt", "r")
ak=f1.readline()
f1.close()

bm=[]
f1=open("blosum50.txt", "r")
for i in range(20):
    line=f1.readline()
    vc=line.split()
    bm.append(vc[:])
for i in range(20):
    for j in range(20):
        bm[i][j]=int(bm[i][j])
f1.close()

x="PAPAHPEWA"
y='PW'
m=len(x)
n=len(y)

sm=[] 
tmp=[]
for i in range(m+1):
    tmp.append(0)
for i in range(n+1):
    sm.append(tmp[:])


for i in range(n+1):
    sm[i][0]=-8*i
for i in range(m+1):
    sm[0][i]=-8*i

aligned_x = ""
aligned_y = ""
print(sm)
i = n
j = m

while i > 0 or j > 0:
    if i > 0 and j > 0:
        score_diag = sm[i-1][j-1]
        bb = bm[ak.index(y[i-1])][ak.index(x[j-1])]
        if sm[i][j] == score_diag + bb:
            aligned_x = x[j-1] + aligned_x
            aligned_y = y[i-1] + aligned_y
            i -= 1
            j -= 1
            continue
    if j > 0 and sm[i][j] == sm[i][j-1] - 8:
        aligned_x = x[j-1] + aligned_x
        aligned_y = '-' + aligned_y
        j -= 1
    elif i > 0 and sm[i][j] == sm[i-1][j] - 8:
        aligned_x = '-' + aligned_x
        aligned_y = y[i-1] + aligned_y
        i -= 1

print("Poravnanje:")
print(aligned_x)
print(aligned_y)
