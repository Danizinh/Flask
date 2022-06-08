import secrets

from flask import Flask, flash, redirect, render_template, request, session


class Jogo:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


# lista global
Jogo_One = Jogo('Tetris', 'Puzzle', 'Atari')
Jogo_Two = Jogo('God of  War', 'Rack n Slash', 'PS2')  # referencia do object
Jogo_three = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [Jogo_One, Jogo_Two, Jogo_three]  # lista reutilizada

app = Flask(__name__)  # referencia ao proprio arquivo
app.secret_key = '23/04/2022'


@app.route('/')  # new rotas
def index():  # definido os dados de visualizacao
    # lista local
    # Referenciando a lista
    # Jogo_One = Jogo('Tetris', 'Puzzle', 'Atari')
    # Jogo_Two = Jogo('God of  War', 'Rack n Slash', 'PS2')
    # Jogo_three = Jogo('Mortal Kombat', 'Luta', 'PS2')
    # lista = [Jogo_One, Jogo_Two, Jogo_three]
    return render_template('lista.html', title='Our Games', jogos=lista)
    # return '<h1>Hello, good morning !! </h1>'
    # return 'Hello, good morning !!'


@app.route('/new')
def new():
    if 'logged in user' not in session or session['logged in user'] == None:
        return redirect('/login?next=new')
    return render_template('new.html', title='New Games')


@app.route('/create', methods=['POST', ])  # rota de processamento do server
def create():
    # obtendo as informacoes do form
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    jogo = Jogo(name, category, console)  # object
    lista.append(jogo)  # referenciando a propria lista
    return redirect('/')
    # return render_template("lista.html", title='Our Games', jogos=lista)


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', title="Run your login", next=next)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if "alohomora" == request.form['password']:
        session['logged in user'] = request.form['user']
        flash(session['logged in user'] + ' user logged in successfully !')
        # return redirect('/')
        next_pag = request.form['next']
        return redirect('/{}'.format(next_pag))  # return route new
    else:
        flash('user not logged in.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['logged in user'] = None
    flash('logout successfully !')
    return redirect('/')


app.run(debug=True)
