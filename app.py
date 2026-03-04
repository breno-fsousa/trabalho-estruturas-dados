from flask import Flask, render_template, request, redirect

app = Flask(__name__)

lista = []
fila = []
pilha = []

@app.route('/')
def home():
    return render_template('index.html', lista=lista, fila=fila, pilha=pilha)


@app.route('/lista/add', methods=['POST'])
def lista_add():
    valor = request.form['valor']
    if valor:
        lista.append(valor)
    return redirect('/')

@app.route('/lista/remove/<int:index>')
def lista_remove(index):
    if 0 <= index < len(lista):
        lista.pop(index)
    return redirect('/')


@app.route('/fila/add', methods=['POST'])
def fila_add():
    valor = request.form['valor']
    if valor:
        fila.append(valor)
    return redirect('/')

@app.route('/fila/remove')
def fila_remove():
    if fila:
        fila.pop(0)
    return redirect('/')


@app.route('/pilha/add', methods=['POST'])
def pilha_add():
    valor = request.form['valor']
    if valor:
        pilha.append(valor)
    return redirect('/')

@app.route('/pilha/remove')
def pilha_remove():
    if pilha:
        pilha.pop()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)