from flask import Flask, render_template

app = Flask(__Glbang2__) # type: ignore

SITE = { # Configurações do site
    'name': 'Zombies',   # Nome do site
    'logo': '',          # Font Awesome de logotipo
    'favicon': '',       # Imagem do favicon
    'owner': 'Glbang2'   # Proprietário da licença do site
}

app.route('/policies')
def policies():
    return "Políticas de privacidade!"

@app.route('/about')
def policies():
    return "Sobre"

@app.route('/contato')
def policies():
    return "contato!"

@app.errorhandler(404)
def errors(e):
    return ('404.html')


if __name__ == '__main__':
    app.run(debug=True)

