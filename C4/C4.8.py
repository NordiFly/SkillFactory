array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)): # проходим по всему массиву
        # count += 1
        idx_min = i # сохраняем индекс предположительно минимального элемента
        for j in range(i+1, len(array)):
                count += 1
                if array[j] < array[idx_min]:

                        idx_min = j
                        # count += 1
        if i != idx_min: # если индекс не совпадает с минимальным, меняем
                array[i], array[idx_min] = array[idx_min], array[i]
                # count += 1

print(array)
print(count)