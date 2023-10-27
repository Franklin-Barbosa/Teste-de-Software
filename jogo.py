class JogoDaVelha:
  def __init__(self):
    self.grade = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.jogador = 1

  def marcar_posicao(self, x, y):
    if not(x >=0 and x < 3 and y >=0 and y < 3 and self.grade[x][y] == 0):
      raise ValueError('Jogada invalida')
    self.grade[x][y] = self.jogador
    # troca jogador
    if self.jogador == 1:
      self.jogador = 2;
    else:
      self.jogador = 1;
    # Retorna True quando a jogada é válida
    return True 

  def vencedor(self):
    for i in range(0, 3):
      # verifica linha
      if self.grade[i][0] != 0 and self.grade[i][0] == self.grade[i][1] and self.grade[i][1] == self.grade[i][2]:
        return self.grade[i][0]
      # verifica coluna
      if self.grade[0][i] != 0 and self.grade[0][i] == self.grade[1][i] and self.grade[1][i] == self.grade[2][i]:
        return self.grade[0][i]
    # verifica diagonal
    if self.grade[0][0] != 0 and self.grade[0][0] == self.grade[1][1] and self.grade[1][1] == self.grade[2][2]:
      return self.grade[0][0]
    # verifica a outra diagonal
    if self.grade[0][2] != 0 and self.grade[0][2] == self.grade[1][1] and self.grade[1][1] == self.grade[2][0]:
      return self.grade[0][2]
    # verifica empate
    contador = 0
    for i in range(0, 3):
      for j in range(0, 3):
        if self.grade[i][j] != 0:
          contador += 1
    if contador == 9:
      return -1 # empate
    return 0 # partida não acabou

def print_grade(grade):
  for l in range(0, 3):
    print(f'{grade[l][0]}|{grade[l][1]}|{grade[l][2]}')
    if l < 2:
      print('-----')

def main():
  jogo = JogoDaVelha()
  print_grade(jogo.grade)
  while jogo.vencedor() == 0:
    print(f'Jogador {jogo.jogador}')
    x = int(input(' Informe a linha: '))
    y = int(input(' Informe a coluna: '))
    try:
      jogo.marcar_posicao(x, y)
    except:
      print('Jogada inválida!')
    print_grade(jogo.grade)
  vencedor = jogo.vencedor()
  if vencedor == -1:
    print('Empate!')
  else:
    print(f'Jogador {vencedor} ganhou!')

if __name__ == "__main__":
  main()

