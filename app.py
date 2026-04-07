from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

   
    perguntas = [
        "A ave está na metade de cima?",
        "Está na linha de cima dessa metade?",
        "A ave está na metade esquerda?",
        "Está na coluna da esquerda dessa metade?"
    ]

    etapa = 0
    respostas = {
        "linha1": None,
        "linha2": None,
        "coluna1": None,
        "coluna2": None
    }

    
    if request.method == "POST" and request.form.get("reset") == "1":
        return render_template(
            "index.html",
            etapa=0,
            pergunta=perguntas[0],
            respostas=respostas
        )

    if request.method == "POST":
        etapa = int(request.form.get("etapa"))

        respostas["linha1"] = request.form.get("linha1")
        respostas["linha2"] = request.form.get("linha2")
        respostas["coluna1"] = request.form.get("coluna1")
        respostas["coluna2"] = request.form.get("coluna2")

        resposta_atual = request.form.get("resposta")

     
        if etapa == 0:
            respostas["linha1"] = resposta_atual
        elif etapa == 1:
            respostas["linha2"] = resposta_atual
        elif etapa == 2:
            respostas["coluna1"] = resposta_atual
        elif etapa == 3:
            respostas["coluna2"] = resposta_atual

        etapa += 1

        
        if etapa == 4:
            aves = [
                ["A", "B", "C", "D"],
                ["E", "F", "G", "H"],
                ["I", "J", "K", "L"],
                ["M", "N", "O", "P"]
            ]

            linha = (0 if respostas["linha1"] == "s" else 2) + (0 if respostas["linha2"] == "s" else 1)
            coluna = (0 if respostas["coluna1"] == "s" else 2) + (0 if respostas["coluna2"] == "s" else 1)

            resultado = aves[linha][coluna]

            return render_template("index.html", resultado=resultado)

    return render_template(
        "index.html",
        etapa=etapa,
        pergunta=perguntas[etapa],
        respostas=respostas
    )


if __name__ == "__main__":
    app.run(debug=True)