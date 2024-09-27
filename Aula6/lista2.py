import os

os.system('cls')

L = ['Alê', 'Marcos', 'Patrick', 'Davi']

L.insert(4, 'Tobby')
print(L)

L.remove('Marcos')
print(L)

L.pop(2)
print(L)

L.sort(reverse=True)
print(L)

L.sort(reverse=False)
print(L)