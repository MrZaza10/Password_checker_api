from fastapi import FastAPI
from pydantic import BaseModel
import re
import string

app = FastAPI(
    title="Password Strength Checker API",
    description="API simples para checar força de senhas!",
    version="1.0.0"
)

class PasswordRequest(BaseModel):
    senha: str

def analisar_senha(senha: str):
    """Retorna (score, categoria, motivos[])"""
    motivos = []
    score = 0
    length = len(senha)

    # regra: tamanho
    if length >= 8:
        score += 2
        motivos.append("Tamanho >= 8")
    elif length >= 6:
        score += 1
        motivos.append("Tamanho >= 6 (melhorar para >=8)")
    else:
        motivos.append("Tamanho < 6 (muito curta)")

    # maiúsculas/minúsculas
    if re.search(r"[A-Z]", senha) and re.search(r"[a-z]", senha):
        score += 2
        motivos.append("Contém maiúsculas e minúsculas!")
    elif re.search(r"[A-Z]", senha) or re.search(r"[a-z]", senha):
        score += 1
        motivos.append("Falta variedade de caixa (maiúsculas/minúsculas)")
    
    # dígitos
    if re.search(r"\d", senha):
        score += 2
        motivos.append("Contém números")

    # símbolos
    if re.search(rf"[{re.escape(string.punctuation)}]", senha):
        score += 2
        motivos.append("Contém caracteres especiais")

    # padrões fracos conhecidos (exemplos simples)
    common_patterns = ["1234", "12345", "password", "senha", "qwerty", "abcd"]
    lower = senha.lower()
    if any(p in lower for p in common_patterns):
        score -= 3
        motivos.append("Contém padrão comum (ex: 123, password)")

    # categoria por score
    if score >= 6:
        categoria = "forte"
    elif score >= 3:
        categoria = "media"
    else:
        categoria = "fraca"
    
    return {"score": score, "categoria": categoria, "motivos": motivos}

@app.post("/verificar")
def verificar_senha(req: PasswordRequest):
    resultado = analisar_senha(req.senha)
    return {"senha": "***", "resultado": resultado}

@app.get("/")
def home():
    return {"Mensagem": "API de Verificação de Senhas está online!"}