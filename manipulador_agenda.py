#tupla que contém os contatos suportados pelo sistema
contatos_suportados = ("telefone", "email", "endereco", "linkedin")

#Dicionário de exemplo, com alguns dados padrão
agenda = {
    "Pessoa 1": {
        "telefone":["11 1234-5678"],
        "email":["pessoa@email.com", "email@profissional.com"],
        "endereco":["Rua 123"],
        "linkedin":["linkedin.com/in/pessoa1"]
},
    "Pessoa 2":{
        "telefone":["11 9874-5678"],
        "email":["pessoa2@email.com", "pessoa2@profissional.com"],
        "endereco":["Rua 345"]
    }
}

def contato_para_texto(nome_contato:str, **formas_contato):
    """Recebe um nome de ontato com string e um dicionário
    com as formas de contato.
    Retorna uma string com os dados recebidos"""
    formato_texto = f"{nome_contato}"
    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas} - {valor.upper()}"
            contador_formas = contador_formas + 1
    return formato_texto
    

#Função de visualização de agenda completa
def agenda_para_texto(**agenda_completa):
    """Recebe um dicionário de dicionários com a agenda que será exibida e retorna o dicionário formatado"""
formato_texto = " "
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto} - {contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}--------------------------------\n"
    return formato_texto

print(agenda_para_texto(**agenda))