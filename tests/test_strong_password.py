import sys
import os

# Adiciona o diretório raiz ao caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from StrongPassword import pontuar_senha, avaliar_nivel

def test_fraca():
    assert pontuar_senha("123", "pessoal") <= 1
    assert avaliar_nivel(1) == "Fraca"

def test_media():
    nota = pontuar_senha("abc123", "pessoal")
    assert 2 <= nota <= 3
    assert avaliar_nivel(nota) == "Média"

def test_forte():
    nota = pontuar_senha("Abc123", "corporativo")
    assert nota == 4
    assert avaliar_nivel(nota) == "Forte"

def test_muito_forte():
    nota = pontuar_senha("Abc123!@ ", "administrativo")
    assert nota == 5
    assert avaliar_nivel(nota) == "Muito Forte"
