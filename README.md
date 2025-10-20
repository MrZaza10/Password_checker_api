# Password Strength Checker API

API desenvolvida em **Python** com **FastAPI** para analisar a força de senhas.

---

## Funcionalidades

- Verifica se a senha é **fraca**, **média** ou **forte**
- Indica os **motivos e critérios** analisados
- Endpoint para requisições **POST via JSON**
- Interface interativa com **Swagger UI**

---

## Tecnologias Utilizadas

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn

---

## Como Executar o Projeto

### 1 Clone o repositório:
   ```bash
   git clone https://github.com/MrZaza10/Password_checker_api.git
   ```

### 2 Acesse o diretório do projeto:
cd Password_checker_api

### 3 Crie e ative o ambiente virtual:
python3 -m venv venv
source venv/bin/activate

### 4 Instale as dependências:
pip install -r requirements.txt

### 5 Execute a aplicação:
uvicorn main:app --reload

### 6 Acesse no navegador:
http://127.0.0.1:8000/docs
