def quadMagic(n):
  #Variáveis para a guardar os valores de soma 
  sumTotal = 0
  sumDiagonal1 = 0
  sumDiagonal2 = 0


  #Cria e preenche a matriz
  matriz = [None]*n
  for i in range(n):
    matriz[i] = [0]*n
  for g in range(n):
    for j in range(n):
      matriz[g][j] = int(input("Digite o valor: "))

  """Checa se é ou não quadrado mágico, a partir de fazer a soma e checar pela igualdade de resultados, soma os valores de linhas e colunas divide por n,
      da matriz nxn, e compara com os valores da soma da diagonal principal e diagonal secundária."""
  for h in range(n):
    for t in range(n):
      if h == t:
        sumDiagonal1 += matriz[h][t]
      sumTotal += matriz[h][t]

  #Loop para a diagonal secundária  
  g = n-1
  h = 0
  while g >= 0:
    sumDiagonal2 += matriz[g][h]
    g -= 1
    h += 1
    
  
  if ((sumTotal/3) == sumDiagonal1) and sumDiagonal1 == sumDiagonal2:
    soma = 0
    for i in range(n):
      soma += matriz[i][0]
    print("É um quadrado mágico de soma ", soma,"!")
    return True
  else:
    print("Não é um quadrado mágico!")
    return


squareSize = int(input("Digite o tamanho do lado do quadrado: "))
quadMagic(squareSize)
