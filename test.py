array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    print("array_i =", array[i], '\t', i)
    for j in range(len(array) - i - 1):
        print("array_j =", array[j], '\t', j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


print(array)