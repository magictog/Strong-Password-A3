import pytest
from strong_password import avaliar_senha

def test_senha_fraca():
    assert avaliar_senha("123") == "Fraca"

def test_senha_media():
    assert avaliar_senha("abcdef") == "Média"

def test_senha_forte():
    assert avaliar_senha("abc12345") == "Forte"

def test_senha_muito_forte():
    assert avaliar_senha("Abc123!@#") == "Muito Forte"