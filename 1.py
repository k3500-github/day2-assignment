li=[ int(n) for n in input().split()]
for num in li:
    if num < 14 and num % 2 != 0:
        print(num)