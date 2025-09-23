# Almix Suplementos

## Descrição do Projeto
Almix Suplementos é uma plataforma web desenvolvida com **Flask** para gerenciar produtos de uma loja de suplementos.  
O projeto permite cadastrar, listar, editar e excluir produtos de forma intuitiva, usando um banco de dados **SQLite** gerenciado pelo **SQLAlchemy**.

---

## Tecnologias Utilizadas
- **Python 3.10+**
- **Flask** – Framework web para Python
- **SQLAlchemy** – ORM para gerenciamento de banco de dados
- **SQLite** – Banco de dados relacional leve
- **HTML/CSS** – Estrutura e estilo do frontend
- **Flask-Login** – Gerenciamento de login e sessão de usuários

---

## Estrutura do Banco de Dados
O projeto possui duas tabelas principais:

### Usuários
Contém informações de login e cadastro dos usuários da plataforma, incluindo nome, email e senha.

### Produtos
Armazena os produtos da loja, com informações como nome, preço e descrição curta.

> O SQLAlchemy permite manipular os dados como objetos, sem precisar escrever SQL manualmente, tornando o código mais limpo e seguro.

---

## Funcionalidades
- Cadastro de usuários com validação de senha.
- Login e logout de usuários.
- CRUD completo de produtos:
  - Cadastrar novos produtos.
  - Listar todos produtos em cards.
  - Editar produtos existentes.
  - Excluir produtos.
- Frontend responsivo e moderno.

---

## Como Rodar o Projeto
1. Clone o repositório:
```

git clone [https://github.com/marcoscassian/AlmixSuplementos.git](https://github.com/marcoscassian/AlmixSuplementos.git)

```
2. Entre na pasta do projeto:
```

cd AlmixSuplementos

```
3. Crie e ative um ambiente virtual:
```

python -m venv env
env\Scripts\activate   # Windows
source env/bin/activate # Linux / macOS

```
4. Instale as dependências:
```

pip install -r requirements.txt

```
5. Execute o projeto:
```

python app.py

```
6. Acesse no navegador:
```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

---

## Integrantes do Projeto
- Marcos Cassiano  
- Alex Bruno  
- Ludimila Erika  
- Isaac Vasconcelos
