#10?4??9
a=[]
for x in range(1004009,1094999+1):
    if str(x)[0:2]=='10' and str(x)[-4]=='4' and str(x)[-1]=='9' and x%151==0:
        a.append(str(x))
print(''.join(a))