#home.py
from flask import render_template, redirect, url_for, session, request
from app.controllers.auth import authenticate, logout # Importe a função authenticate corretamente
from . import routes_bp
from app.models.fornecedor import Fornecedor # Importe o modelo Fornecedor
from app.models.Produto import Produto # Importe o modelo Fornecedor
from app.models import db # Importe o objeto db do módulo app.models

# Rota para a página inicial
@routes_bp.route('/')
def index():
  return render_template('login.html')
# Rota para a autenticação do usuário
@routes_bp.route('/auth', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
   username = request.form['username']
password = request.form['password']
if authenticate(username, password): # Chama a função authenticate corretamente
 print("Autenticação bem-sucedida")
return redirect(url_for('routes.welcome')) # Redireciona para /welcome se a autenticação for bem-sucedida
else:
return render_template('login.html', error="Invalid username or password")
else:

return render_template('login.html')
# Rota para a página de boas-vindas
@routes_bp.route('/welcome')
def welcome():
if 'username' in session:
return render_template('welcome.html', username=session['username'], user_type=session['user_type'])
else:
return redirect(url_for('login'))
# Rota para logout do usuário
@routes_bp.route('/logout')
def logout():
logout() # Chama a função logout corretamente
return redirect(url_for('login'))
# Rota para a página de fornecedores
from app.models import Fornecedor # Importe o modelo Fornecedor
@routes_bp.route('/fornecedores')
def fornecedores():
fornecedores = Fornecedor.query.all() # Buscar todos os fornecedores do banco de dados
return render_template('fornecedores.html', fornecedores=fornecedores)
@routes_bp.route('/editar_fornecedor/<int:fornecedor_id>')
def edit_fornecedor(fornecedor_id):
fornecedor = Fornecedor.query.get_or_404(fornecedor_id) # Buscar o fornecedor com o ID fornecido
return render_template('editar_fornecedor.html', fornecedor=fornecedor, fornecedor_id=fornecedor_id)

@routes_bp.route('/atualizar_fornecedor/<int:fornecedor_id>', methods=['POST'])
def update_fornecedor(fornecedor_id):
fornecedor = Fornecedor.query.get_or_404(fornecedor_id) # Buscar o fornecedor com o ID fornecido
# Atualizar os campos do fornecedor com os dados do formulário enviado
fornecedor.Fornecedor = request.form['Fornecedor']
fornecedor.telefone = request.form['telefone']
fornecedor.revendedor = request.form['revendedor']