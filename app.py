from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template(
        "index.html",
        nom_site="PRINCE STORE",
        telephone="+509 38 18 02 18",
        email="alphapro441@gmail.com"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
