l = int(input("Quantas Lavagem realizadas: "))
v = float(input("Valor da Lavagem: "))
t = l * v

print (f'Foi realizado %d lavagem no valor de R$ %.2f gerando um total de R$ %.2f' % (l,v,t))