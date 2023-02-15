x = int(input("digite um numero!"))

numeros = [i for i in range(1,x+1)]

primos = [k for k in numeros if x % k == 0]

if len(primos) > 2:
    print("numero não é primo")
else:
    print("numero primo")