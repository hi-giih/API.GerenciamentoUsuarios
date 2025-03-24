from flask import Flask, request, jsonify
from models.user import User

app = Flask(__name__)

users = []
id_control_user = 1

@app.route('/users', methods=["POST"])
def create_user():
    global id_control_user
    dado = request.get_json()
    new_user = User(id=id_control_user, nome=dado['nome'], idade=dado['idade'], email=dado['email'])
    if not dado['nome']:
        return jsonify({"message":"Os dados enviados são inválidos ou incompletos: Nome"}), 400
    elif len(dado['nome']) < 3 or len(dado['nome']) > 50:
        return jsonify({"message":"O nome deve ter entre 3 e 50 caracteres"}), 400
    elif int(dado['idade']) <8 or int(dado['idade']) > 100:
        return jsonify({"message":"A idade deve estar entre 8 e 100 anos"}), 400
    elif not dado['email']:
        return jsonify({"message": "Os dados enviados são inválidos ou incompletos: Email"}), 400
    else:
        email_existe = False
        for u in users:
            if u.email == dado['email']:
                 email_existe = True
                 break
        
        if email_existe == True:
            return jsonify({"message":"O email informado já está cadastrado"}), 400
        else:
            users.append(new_user)
        print(dado)
        id_control_user += 1
        return jsonify({"message":"Usuario criado com sucesso"})

@app.route('/users', methods=['GET'])
def get_users():
    nomes = [user.nome for user in users]
    if not nomes:
        return jsonify({"message":"A lista está vazia"})

    retorno = {
            "nomes":nomes,
            "total_user":len(nomes)
        }
    return jsonify(retorno)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    for u in users:
        if u.id == id:
            return jsonify(u.to_dict())
    
    return jsonify({"message":"Usuario não existe"}), 404


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    useer = None
    for u in users:
        if u.id == id:
            useer= u

    if useer == None:
        return jsonify({"message": "Não foi possivel encontrar o usuario"}),404
        
    dado = request.get_json()
    if not dado.get('nome') or len(dado['nome']) < 3 or len(dado['nome']) > 50:
        return jsonify({"message": "O nome deve ter entre 3 e 50 caracteres"}), 400
    if not dado.get('idade') or int(dado['idade']) < 8 or int(dado['idade']) > 100:
        return jsonify({"message": "A idade deve estar entre 8 e 100 anos"}), 400
    if not dado.get('email'):
        return jsonify({"message": "Email é obrigatório"}), 400

    useer.nome = dado['nome']
    useer.idade = dado['idade']
    useer.email = dado['email']
    return jsonify({"message": "Usuario atualizado com sucesso"})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    useer = None
    for u in users:
        if u.id == id:
            useer= u
            break

    if useer == None:
        return jsonify({"message": "Não foi possivel encontrar esse usuario"}),404
        
    users.remove(useer)
    return jsonify({"message": "Usuario deletada com sucesso"})

if __name__=='__main__':
    app.run(debug=True) 