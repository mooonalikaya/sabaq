#1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)


#2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elements = []
for i in a:
    if i in b and i not in elements:
        elements.append(i)

print(elements)

#3
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def get_value(item):
    return item[1]

sorted_ascending = {k: v for k, v in sorted(d.items(), key=get_value)}
print("Сортировка по значениям (возрастание):", sorted_ascending)

sorted_descending = {k: v for k, v in sorted(d.items(), key=get_value, reverse=True)}
print("Сортировка по значениям (убывание):", sorted_descending)
