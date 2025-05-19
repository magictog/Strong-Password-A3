from StrongPassword import pontuar_senha, avaliar_nivel

def test_senha_fraca():
    assert pontuar_senha("123", "pessoal") == 1
    assert avaliar_nivel(1) == "Fraca"

def test_senha_media():
    senha = "abc123"
    nota = pontuar_senha(senha, "pessoal")
    assert 2 <= nota <= 3
    assert avaliar_nivel(nota) == "Média"

def test_senha_forte():
    senha = "Abc123"
    nota = pontuar_senha(senha, "corporativo")
    assert nota == 4
    assert avaliar_nivel(nota) == "Forte"

def test_senha_muito_forte():
    senha = "Abc123!@ "
    nota = pontuar_senha(senha, "administrativo")
    assert nota == 5
    assert avaliar_nivel(nota) == "Muito Forte"
