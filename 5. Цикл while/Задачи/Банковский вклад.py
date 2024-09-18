start_sum=int(input())
percent=int(input())
target_sum=int(input())
a=0
while start_sum<target_sum:
    start_sum+=start_sum*percent/100
    a+=1
    print(f"{a} - {start_sum:0.2f}")





