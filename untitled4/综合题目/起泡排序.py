def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            break
if __name__ == '__main__':
    alist = [94, 26, 93, 57, 44, 31, 443, 55, 204]
    print("原列表为：%s" % alist)
    bubble_sort(alist)
    print("新列表为：%s" % alist)
