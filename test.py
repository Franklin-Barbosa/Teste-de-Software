import unittest
from jogo import JogoDaVelha

class TesteJogoDaVelha(unittest.TestCase):
    def test_jogada_valida(self):
        jogo = JogoDaVelha()
        self.assertTrue(jogo.marcar_posicao(0, 0))

    def test_jogada_invalida_fora_limites(self):
        jogo = JogoDaVelha()
        with self.assertRaises(ValueError):
            jogo.marcar_posicao(3, 3)

    def test_jogada_invalida_posicao_ocupada(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        with self.assertRaises(ValueError):
            jogo.marcar_posicao(0, 0)

    def test_vitoria_horizontal_jogador_1(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(1, 0)
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(0, 2)
        self.assertEqual(jogo.vencedor(), 1)

    def test_vitoria_horizontal_jogador_2(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0,0)
        jogo.marcar_posicao(1,0)
        jogo.marcar_posicao(0,2)
        jogo.marcar_posicao(0,1)
        jogo.marcar_posicao(2,2)
        jogo.marcar_posicao(1,2)
        jogo.marcar_posicao(2,1)
        jogo.marcar_posicao(1,1)
        self.assertEqual(jogo.vencedor(), 2)

    def test_vitoria_vertical_jogador_1(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(1, 0)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(2, 0)
        self.assertEqual(jogo.vencedor(), 1)

    def test_vitoria_vertical_jogador_2(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0,0)
        jogo.marcar_posicao(1,0)
        jogo.marcar_posicao(0,1)
        jogo.marcar_posicao(1,1)
        jogo.marcar_posicao(2,2)
        jogo.marcar_posicao(1,2)
        self.assertEqual(jogo.vencedor(),2)

    def test_vitoria_diagonal_superior_esquerda_para_direita_jogador_1(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(0, 2)
        jogo.marcar_posicao(2, 2)
        self.assertEqual(jogo.vencedor(), 1)

    def test_vitoria_diagonal_superior_esquerda_para_direita_jogador_2(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(0, 2)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(2, 0)
        jogo.marcar_posicao(2, 2)
        self.assertEqual(jogo.vencedor(), 2)

    def test_vitoria_diagonal_superior_direita_para_esquerda_jogador_1(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 2)
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(2, 0)
        self.assertEqual(jogo.vencedor(), 1)

    def test_vitoria_diagonal_superior_direita_para_esquerda_jogador_2(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(0, 2)
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(1, 0)
        jogo.marcar_posicao(2, 0)
        self.assertEqual(jogo.vencedor(), 2)

    def test_sem_vencedor(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(1, 0)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(2, 2)
        jogo.marcar_posicao(0, 2)
        jogo.marcar_posicao(1, 2)
        jogo.marcar_posicao(2, 1)
        jogo.marcar_posicao(2, 0)
        self.assertEqual(jogo.vencedor(), 1)

    def test_empate(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        jogo.marcar_posicao(0, 1)
        jogo.marcar_posicao(0, 2)
        jogo.marcar_posicao(1, 1)
        jogo.marcar_posicao(1, 0)
        jogo.marcar_posicao(1, 2)
        jogo.marcar_posicao(2, 1)
        jogo.marcar_posicao(2, 0)
        jogo.marcar_posicao(2, 2)
        self.assertEqual(jogo.vencedor(), -1)

    def test_alternancia_de_turno(self):
        jogo = JogoDaVelha()
        jogo.marcar_posicao(0, 0)
        self.assertEqual(jogo.jogador, 2)
        jogo.marcar_posicao(0, 1)
        self.assertEqual(jogo.jogador, 1)

if __name__ == "__main__":
    unittest.main()
