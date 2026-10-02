import bermuda
from flask import Flask, render_template, request
app = Flask (__name__)
tarefas = []
@app.route('/')
def home():
    return render_template('index.html') # Pagina inicial do site


@app.route('/sobre')
def sobre():
    return 'Esta é a pagina sobre o projeto.'

@app.route('/tarefas', methods=['GET', 'POST'])
def lista_tarefa():
    if request.method == 'POST':
        nome_tarefa = request.form['Tarefa']
        tarefas.append(nome_tarefa)
        print(nome_tarefa)
    return render_template('tarefas.html', tarefas=tarefas)

if __name__=='__main__':
    app.run(debug=True)


#<ul>
#{% for ___ in ___ %}
 #   <li>{{ ___ }}</li>
#{% endfor %}
#</ul>
