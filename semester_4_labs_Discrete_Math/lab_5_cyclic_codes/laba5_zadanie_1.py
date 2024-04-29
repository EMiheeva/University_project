import sys
import numpy as np
from tabulate import tabulate
np.set_printoptions(threshold=sys.maxsize)
g = [int(i) for i in "10011"]  # порождающий многочлен
n = 15  # общее число элементов
m = 11  # число информационных элементов
length = len(g)
for i in range(n - length):
     g.append(0)
G0 = []  # временная матрица
for i in range(m):
     G0.append(np.roll(g, i))
G = np.array(G0)  # порождающая матрица
codewords_table_headers = ["Информационное слово", "Кодовое слово"] #Столбец кодовое слово - это и есть порождающая матрица!
codewords_table = []
length = pow(2, m)
for i in range(0, length):
     d = np.array([int(i) for i in np.binary_repr(i, m)])
     codewords_table.append([''.join(map(str, d.tolist())), ''.join(map(str, np.mod(d.dot(G), 2)))])
with open('output1.txt', 'w') as file:
     file.write("Разрешенные кодовые комбинации: ")
     file.write("\n")
     file.write(tabulate(codewords_table, codewords_table_headers, tablefmt="grid", numalign='center'))
     file.close()
     print("Посмотреть файл output.txt")
