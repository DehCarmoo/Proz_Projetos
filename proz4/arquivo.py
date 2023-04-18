def idade(nome, ano_nascimento):
  try:
    if (ano_nascimento > 1921 and ano_nascimento <= 2022):
      valor_idade = 2023 - ano_nascimento
      valor_idade2 = 2022 - ano_nascimento
      print("Seja bem-vindo(a),", nome, ", seu ano de nascimento é:", ano_nascimento, "Se você já fez aniversário no ano de (2023), você tem", valor_idade, "anos. Caso ainda não tenha feito aniversário, sua idade é", valor_idade2, "anos.")
    else:
      print("Ano de nascimento inválido")
      ano_nascimento = int(input("Por favor, digite novamente seu ano de nascimento: "))
      idade(nome, ano_nascimento)
  except:
    print("Ano de nascimento inválido")
    
    

nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
idade(nome, ano_nascimento)