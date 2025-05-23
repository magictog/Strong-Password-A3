import unittest
from strong_password.core import pontuar_senha, avaliar_nivel

class TestStrongPassword(unittest.TestCase):
    def test_pontuar_senha(self):
        self.assertEqual(pontuar_senha("senha"), 1)
        self.assertEqual(pontuar_senha("Senha123"), 3)
        self.assertEqual(pontuar_senha("Senha123!@#"), 4)
        self.assertEqual(pontuar_senha("Senha123!@#longa"), 5)

    def test_avaliar_nivel(self):
        self.assertEqual(avaliar_nivel(1), "Fraca")
        self.assertEqual(avaliar_nivel(2), "Fraca")
        self.assertEqual(avaliar_nivel(3), "Média")
        self.assertEqual(avaliar_nivel(4), "Média")
        self.assertEqual(avaliar_nivel(5), "Forte")

if __name__ == '__main__':
    unittest.main()
