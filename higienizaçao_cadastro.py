nome = " leonardo carreon "
email = " leonardo.carreon@ecolinha.com "

nome_higienizado = nome.strip().upper()
email_higienizado = email.strip().lower()

print("Nome higienizado:", nome_higienizado)
print("E-mail higienizado:", email_higienizado)

cpf = " 123.456.789-00 "
telefone = "(11) 996767-2828"

cpf_limpo = (
    cpf.strip()
    .replace(".", "")
    .replace("-", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
)

telefone_limpo = (
    telefone.strip()
    .replace(".", "")
    .replace("-", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
)

print("CPF limpo:", cpf_limpo)
print("Telefone limpo:", telefone_limpo)

codigo = " prod-1024-br-sp "

codigo_formatado = codigo.strip().upper().replace("-", "_")

print("Código formatado:", codigo_formatado)