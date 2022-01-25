def solve(n, s):
    ind1, ind2 = 0, len(n) - 1
    while s != n:
        if n[ind1] + n[ind2] > s:
            ind2 -= 1
        elif n[ind1] + n[ind2] < s:
            ind1 += 1
        else:
            print(f'Found {n[ind1]}, {n[ind2]}')
            break

num = list(map(int, input().split()))
su = int(input())
sorted(num)

solve(num, su)
