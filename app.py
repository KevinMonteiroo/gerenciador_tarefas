from flask import Flask, render_template
app = Flask (__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return 'Esta é a pagina sobre o projeto.'

@app.route('/tarefas')
def tarefas():
    return 'Aqui vão aparecer mais tarefas.'

if __name__=='__main__':
    app.run(debug=True)

