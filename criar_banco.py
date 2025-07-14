from fakepinterest import detabase, app
from fakepinterest.models import Usuario, Foto
# Criar a estrutura do banco de dados

with app.app_context():
    detabase.create_all()