from flask import Flask, render_template, request
app = Flask (__name__)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return 'Esta é a pagina sobre o projeto.'

@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
    if request.method == 'POST':
        nome_target = request.form['Tarefa']
        print(nome_target)
    return render_template('tarefas.html')

if __name__=='__main__':
    app.run(debug=True)

