#Dado o número de moedas e o valor de cada moeda, informe o valor recebido.
#sua resposta
print('digite a quantidade moedas você entregou:')
qtd = int(input())
soma= 0

for i in range(qtd):
  print('digite as moedas:')
  moedas = float(input())
  soma = moedas + soma

print(soma,)
