x = int(input())
y = int(input())
z = int(input())
ml = int(input())
t1 = int((x/(3*16.66))+(y/(2*16.66))+(z/(6*16.66)))
t2 = int((x/(3*16.66))+(y/(6*16.66))+(z/(2*16.66)))
print('6' + ' ' + str(t1))
print(str(6+t2//60) + ' ' + str(t2%60))
