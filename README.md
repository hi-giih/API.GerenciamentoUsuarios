# 👥 CRUD com Flask - Gestão de Usuários

## 📄 Descrição
Este projeto é um exemplo simples de CRUD (Create, Read, Update, Delete) utilizando o microframework Flask em Python. Ele permite criar, visualizar, atualizar e excluir usuários através de requisições HTTP. Esse projeto foi desenvolvido como parte do aprendizado de desenvolvimento de APIs com Flask.

---

## ⚙️ Funcionalidades
- **Criar Usuário:** Adiciona um novo usuário à lista com nome, idade e e-mail.
- **Visualizar Todos os Usuários:** Retorna todos os usuários cadastrados.
- **Visualizar um Usuário Específico:** Exibe os detalhes de um usuário pelo seu ID.
- **Atualizar Usuário:** Modifica as informações de um usuário existente.
- **Deletar Usuário:** Remove um usuário da lista.

---

## 💻 Tecnologias Utilizadas
- **Python 3.11:** Linguagem utilizada para o desenvolvimento da aplicação.
- **Flask 2.3.0:** Framework de desenvolvimento web utilizado para criar a aplicação e gerenciar rotas HTTP.

---

## 🚀 Instalando e Rodando o Projeto

1. Clone este repositório:
```
git clone git@github.com:hi-giih/API.GerenciamentoUsuarios.git
```

2. Acesse o diretório do projeto:
```
cd API.GerenciamentoUsuario
```

3. Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
```

4. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

5. Instale as dependências:
```
pip install -r requeriments.txt
```

6. Execute o projeto:
```
python app.py
```
O servidor estará disponível em: `http://127.0.0.1:5000`

---

## 🔧 Futuras Melhorias
- Implementação de persistência de dados com um banco de dados (SQLite, PostgreSQL, etc.).
- Autenticação e autorização para maior segurança.
- Validações mais robustas nas requisições.
- Interface gráfica com HTML/CSS para interação com o usuário.

---

## 📜 Licença
Este projeto não está sob nenhuma licença específica.

