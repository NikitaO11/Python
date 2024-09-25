def number(b):
    a=[]
    for i in range(2,b+1):
        k=0
        for j in range(1, i+1):
            if i%j ==0:
                k+=1
        if k == 2:
            a.append(i)
    end=""
    col=int(input("Введите число"))
    g=a[:col]
    print(g)
number(1000)



