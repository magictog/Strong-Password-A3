def pontuar_senha(senha):
    pontuacao = 0
    if any(char.islower() for char in senha):
        pontuacao += 1
    if any(char.isupper() for char in senha):
        pontuacao += 1
    if any(char.isdigit() for char in senha):
        pontuacao += 1
    if any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in senha):
        pontuacao += 1
    if len(senha) >= 12:
        pontuacao += 1
    return pontuacao

def avaliar_nivel(pontuacao):
    if pontuacao <= 2:
        return "Fraca"
    elif pontuacao == 3 or pontuacao == 4:
        return "Média"
    elif pontuacao == 5:
        return "Forte"
