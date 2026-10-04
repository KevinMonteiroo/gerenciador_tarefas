import bermuda
from flask import Flask, render_template, request, redirect

app = Flask (__name__)
tarefas = []
@app.route('/')
def home():
    return render_template('index.html') # Pagina inicial do site


@app.route('/sobre')
def sobre():
    return 'Esta é a pagina sobre o projeto.'

@app.route('/tarefas', methods=['GET', 'POST'])#rota necessária para receber os dados do formulário
def lista_tarefa(): #só busca o dado do formulário quando ele foi enviado, evita erro quando a página só é aberta
    if request.method == 'POST':
        nome_tarefa = request.form['Tarefa']
        tarefas.append(nome_tarefa)
        print(nome_tarefa)
    return render_template('tarefas.html', tarefas=tarefas)


@app.route('/remover/<int:posicao>')
def remover_tarefa(posicao):
    tarefas.pop(posicao)

    return redirect('/tarefas')

if __name__=='__main__':
    app.run(debug=True)



