from flask import Flask, request, render_template_string
from strong_password import avaliar_senha  # adaptar conforme nome do módulo real

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        senha = request.form.get("senha")
        resultado = avaliar_senha(senha)  # função que analisa senha
    return render_template_string("""
        <form method="post">
            Digite sua senha: <input name="senha" type="text">
            <input type="submit">
        </form>
        <p>{{ resultado }}</p>
    """, resultado=resultado)

if __name__ == "__main__":
    app.run()
