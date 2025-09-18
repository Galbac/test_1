n = int(input('Введите количество элементов: '))
result = []
num = 1

while len(result) < n:
    result.extend([num]*num)
    num += 1
print(''.join(map(str, result[:n])))