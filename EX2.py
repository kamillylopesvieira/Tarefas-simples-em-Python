# Dado um número de apostas realizadas por uma pessoa e o valor de cada uma, informe quanto a pessoa gastou com apostas
# Resposta
print('digite a quantidade apostas feitas:')
qtd = int(input())
soma= 0

for i in range(qtd):
  print('digite o valor gasto:')
  valor = float(input())
  soma = valor + soma

print(soma,)
