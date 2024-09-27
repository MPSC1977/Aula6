import os

os.system('cls')

# for e in range(0, 100, 10):
#     print(e)

# nome = 'Marcos'
# for e in nome:
#     print(e)

# nome = [1, 2, 'Oi', 3.5]
# for e in nome:
#     print(e)

# i = int(input('Valor :'))
# f = int(input('Valor final :'))

# s = 0
# for e in range(5):
#     n = int(input('Valor :'))
#     s = s + n
# print(f'O total é {s}')    

# for e in range(10, -1, -1):
#     print(e)

n = int(input('Informe um número: '))

for e in range(1, n+1):
    if n % e == 0:
        print(e)
    


