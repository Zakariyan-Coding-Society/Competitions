weight = int(input())
# Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.
even = list(range(2,weight, 2))
ind_1, ind_2, flag = 0, len(even)-1 , 0
while ind_1<=ind_2:
    if even[ind_1]+even[ind_2] > weight:
        ind_2 -= 1
    elif even[ind_1]+even[ind_2] < weight:
        ind_1 += 1
    else:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")


