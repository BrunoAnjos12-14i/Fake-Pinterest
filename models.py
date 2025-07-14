#Criar a estrutura do banco de dados
from fakepinterest import detabase
from datetime import datetime

# ...existing code...
class Usuario(detabase.Model):
    id = detabase.Column(detabase.Integer, primary_key=True)
    username = detabase.Column(detabase.String, nullable=False, unique=True)
    email = detabase.Column(detabase.String, nullable=False, unique=True)
    senha = detabase.Column(detabase.String, nullable=False)
    postagem = detabase.relationship("Foto", backref="usuario", lazy=True)

class Foto(detabase.Model):
    id = detabase.Column(detabase.Integer, primary_key=True)
    imagem = detabase.Column(detabase.String, default='default.png')
    data_criacao = detabase.Column(detabase.DateTime, default=datetime.utcnow)
    id_usuario = detabase.Column(detabase.Integer, detabase.ForeignKey('usuario.id'), nullable=False)
# ...existing code...