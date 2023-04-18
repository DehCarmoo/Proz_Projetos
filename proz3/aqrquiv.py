def calculadora(valor1, valor2, op):
  if(op == 1):
    resultado = valor1 + valor2
    print(valor1, "+", valor2, "=", resultado)
  elif(op == 2):
    resultado = valor1 - valor2
    print(valor1, "-", valor2, "=", resultado)
  elif(op == 3):
    resultado = valor1 * valor2
    print(valor1, "x", valor2, "=", resultado)
  elif(op == 4):
    resultado = valor1 / valor2
    print(valor1, "/", valor2, "=", resultado)
  else: 
    print(0)

calculadora(100, 2, 4) 