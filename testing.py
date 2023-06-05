alist = [1,2,3]
blist = [3,2,3]
clist = [3,3,3]


# for num in alist:
#     print(num)
#     for num2 in alist[1:]:
#         pass
#     if num != num2:
#         count += num
#     if


def check(somelist):
    count = 0
    if somelist[0] not in somelist[1:]:
        return sum(somelist)
    else:
        if somelist[0] != somelist[1] and somelist[0] != somelist[2]:
            count += somelist[0]
        if somelist[1] != somelist[2] and somelist[1] != somelist[0]:
            count += somelist[1]
        if somelist[2] != somelist[0] and somelist[2] != somelist[1]:
            count += somelist[2]
        return count


print(check(clist))