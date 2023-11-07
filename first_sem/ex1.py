# 27. все элементы, перед которыми стоит отрицательное число, увеличить на 5.
def func(lst):
    for index in range(1, len(lst)):
        if lst[index - 1] < 0:
            lst[index] += 5


result = list(map(int, input().split()))
func(result)
print(result)