from flask import Flask
app = Flask (__name__)
@app.route('/')
def home():
    return 'Olá, Mundo!'

@app.route('/sobre')
def sobre():
    return 'Esta é a pagina sobre o projeto.'

@app.route('/tarefas')
def tarefas():
    return 'Aqui vão aparecer mais tarefas.'

if __name__=='__main__':
    app.run(debug=True)

