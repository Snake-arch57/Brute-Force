import hashlib
 
def login(usuario, senha):
    if (hashlib.sha1(usuario.encode()).hexdigest() == "dc76e9f0c0006e8f919e0c515c66dbba3982f785" and
        hashlib.sha1(senha.encode()).hexdigest() == "a7d579ba76398070eae654c30ff153a4c273272a"):
        return ('Logado')
    else:
        return ('Usuário não encontrado')
 
 
 
user = [

    'admin', 'admin1', 'administrador', 'convidador',

    'root', 'guest',

]
 
senha = [

    'dor', 'pain', 'fiap', '123456', 'painless',

    '12345678', '87654321', '354687'

]

try:
    for u in user:
        for s in senha:
            resultado = login(u,s)
            if resultado == "Logado":
                print(f'usuário: {u}, senha: {s}')
            else:
                print('É outra coisa ')    
except IndexError:
    print('ERRO 404')
