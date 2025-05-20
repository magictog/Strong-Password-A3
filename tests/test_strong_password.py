import unittest
from strong_password import avaliar_senha  # Supondo que essa seja sua função de análise

class TestStrongPassword(unittest.TestCase):

    def test_senha_fraca(self):
        self.assertEqual(avaliar_senha("12345"), 1)  # Exemplo de senha fraca

    def test_senha_media(self):
        self.assertEqual(avaliar_senha("abc123"), 3)  # Exemplo de senha média

    def test_senha_forte(self):
        self.assertEqual(avaliar_senha("A1b@cD#4e"), 5)  # Exemplo de senha forte

if __name__ == "__main__":
    unittest.main()