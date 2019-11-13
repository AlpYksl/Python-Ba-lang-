# 4 milyona kadar olan çift fibonacci sayılarının toplamı
T1,T2,T3 = 1,1,0
Result = 0
while T3<4000000:
    T3 = T1+T2
    if T3%2==0:
        Result += T3
    T1 = T2
    T2 = T3

    print(Result)
