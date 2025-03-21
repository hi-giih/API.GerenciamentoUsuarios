class User():
    def __init__(self, id, nome, idade, email) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email
        }