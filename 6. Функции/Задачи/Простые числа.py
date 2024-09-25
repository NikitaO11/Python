def is_simple(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
a=int(input())
count = 0
b=2
while count < a:
    if is_simple(b):
        print(f"{b}", end=" ")
        count +=1
    b +=1
