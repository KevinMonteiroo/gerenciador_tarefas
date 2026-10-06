from flask import Flask, render_template, request, redirect,flash

app = Flask (__name__)
app.secret_key = 'chave_secreta_qualquer'
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
        if nome_tarefa != '':
            tarefas.append({'nome': nome_tarefa, 'concluida': False})
        else:
            flash('O campo esta vazio')
        print(nome_tarefa)
    return render_template('tarefas.html', tarefas=tarefas)


@app.route('/remover/<int:posicao>')
def remover_tarefa(posicao):
    tarefas.pop(posicao)

    return redirect('/tarefas')

@app.route('/concluir/<int:posicao>')
def concluir_tarefa(posicao):
    tarefas[posicao]['concluida'] = True

    return redirect('/tarefas')

if __name__=='__main__':
    app.run(debug=True)



