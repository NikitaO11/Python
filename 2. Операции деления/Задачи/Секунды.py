a = int(input())
h = a // 3600
s = a % 3600
m = s // 60
s = s % 60
print(h, m, s, sep=":")
