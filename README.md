# 🔐 Strong Password - Verificador de Força de Senhas

Este projeto tem como objetivo ajudar usuários a criarem senhas mais seguras com base em critérios de complexidade e contexto de uso. A aplicação foi desenvolvida em Python como parte da disciplina **Modelos, Métodos e Técnicas de Engenharia de Software – 2025/1**, incorporando boas práticas de segurança, modularização, testes automatizados e integração contínua via GitHub Actions.

---

## 📌 Funcionalidades

- Verificação de força da senha (pontuação de 0 a 5)
- Análise de tipos de caracteres: minúsculas, maiúsculas, números, espaços e símbolos
- Requisitos mínimos de segurança ajustados conforme o contexto de uso
- Recomendações automáticas para melhorar senhas fracas
- Compatível com Windows, Linux e MacOS (executado via terminal)

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/magictog/Strong-Password-A3.git
   cd Strong-Password-A3

2. Execute o programa com:
    python StrongPassword.py

3. Escolha um contexto e digite sua senha de forma segura para avaliação.

## 🧪 Testes Automatizados
Este projeto conta com testes unitários usando pytest.

Para rodar localmente:
    pip install pytest
    pytest

## 🔁 Integração Contínua (CI/CD)
A aplicação conta com um pipeline configurado no GitHub Actions que realiza:

- Instalação automática das dependências

- Execução dos testes unitários a cada push ou pull request

- Validação contínua da qualidade do código

## 👥 Equipe de Desenvolvimento
Enrico Aguiar Vrunski

Thiago Ferreira Lima Gonçalves

Matheus Tognon Siqueira

Felipe Soares de Oliveira

Gabriel de Almeida Carmo

## 📄 Licença
Este projeto é de caráter educacional, sem fins comerciais, e integra as entregas da disciplina Modelos, Métodos e Técnicas da Engenharia de Software do curso de Tecnologia Sistemas de Informação.

## 📚 Referências Técnicas
- [Python Docs - string](https://docs.python.org/3/library/string.html)

- [Python Docs - getpass](https://docs.python.org/3/library/getpass.html)

- [GitHub Actions](https://docs.github.com/en/actions)








