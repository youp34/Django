#顺序查找
def line_search(lst, val):
    for index, value in enumerate(lst):
        if val == value:
            return index
    return None
# 二分查找
def binary_search(lst, val):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (high + low)//2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return None
if __name__ == '__main__':
    lst = list(range(100000))
    ret = line_search(lst, 90000)
    print(ret)
    ret = binary_search(lst, 90000)
    print(ret)