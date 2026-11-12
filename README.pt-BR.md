# 📒 Agenda de Contatos em Python

## 📖 Sobre o Projeto

Este projeto consiste em uma aplicação simples desenvolvida em Python para gerenciamento e exibição de contatos.

A aplicação armazena informações utilizando estruturas de dados nativas da linguagem, permitindo organizar diferentes formas de contato, como telefone, e-mail, endereço e LinkedIn, de maneira flexível e escalável.

O objetivo principal foi praticar conceitos fundamentais de programação e manipulação de dados utilizando Python.

---

## 🎯 Objetivo

Desenvolver uma aplicação capaz de organizar e exibir informações de contatos de forma estruturada, reforçando conhecimentos em:

- Estruturas de Dados
- Funções
- Manipulação de Dicionários
- Tuplas
- Laços de Repetição
- Formatação de Saída

---

## 💡 Problema Resolvido

Em muitas situações, um contato pode possuir múltiplas formas de comunicação, como vários telefones ou diferentes e-mails.

Este projeto resolve essa necessidade utilizando uma estrutura baseada em dicionários e listas, permitindo armazenar múltiplos meios de contato para uma mesma pessoa de forma organizada e de fácil consulta.

---

## 🚀 Funcionalidades

✅ Cadastro estruturado de contatos

✅ Suporte para múltiplos telefones

✅ Suporte para múltiplos e-mails

✅ Inclusão de endereço

✅ Inclusão de perfil do LinkedIn

✅ Exibição formatada dos dados

✅ Estrutura preparada para futura expansão

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Estruturas de Dados Nativas
- Dicionários (`dict`)
- Tuplas (`tuple`)
- Listas (`list`)
- Funções
- Parâmetros Nomeados (`**kwargs`)

---

## 🧠 Conceitos Aplicados

### Tuplas

Utilizadas para armazenar os tipos de contato suportados pelo sistema:

```python
contatos_suportados = (
    "telefone",
    "email",
    "endereco",
    "linkedin"
)
```

---

### Dicionários

Utilizados para organizar os contatos e suas informações.

```python
agenda = {
    "Pessoa 1": {
        "telefone": ["11 1234-5678"],
        "email": ["pessoa@email.com"]
    }
}
```

---

### Funções

O projeto utiliza funções para separar responsabilidades e facilitar a manutenção do código.

```python
contato_para_texto()
agenda_para_texto()
```

---

### Parâmetros Dinâmicos

Utilização de `**kwargs` para receber quantidades variáveis de informações.

```python
def contato_para_texto(nome_contato, **formas_contato):
```

---

### Iteração sobre Estruturas de Dados

Uso de laços para percorrer dicionários e listas.

```python
for meio_contato, contato in formas_contato**tems():
**`

---

## 📂 Estrutura do Projet***```text
agenda-com**eta/
│
├── agenda.py
**─ README.md
```

---

## ▶**Como Executar

Clone** repositório:

```bash
git clone**ttps://github.com/sandrefilipedev/agenda_completa.git
```

**esse a pasta do projeto:

```bash*** agenda_completa
```

Execute a a**icação:

```bash
python agenda.py**``

**-

## 📊 Exemplo de Saída**```text
Pessoa 1

**LEFONE
   ** - 11 1234-567**
EMAIL
    1 - P**SOA@EMAIL.COM
    **- EMAIL@PROFISSIONAL.COM

**DERECO
    1 - R** 123

LINKEDIN
   ** - LINKEDIN.COM/IN/P**SOA1
```

---

## 📚**prendizados

Durante o**esenvolvimento deste projeto fora**pratic**os os seguintes conceitos:

- Est***uras de Dados em Python
- Model**em de Informações
- Manipulação d**Dicionários Aninhados
- Cr**ção e Organização de Funções
**Parâmetros Vari**eis (`**kwargs`)
- Formatação de ****a de Dados
- Bo** Práticas de Leg**ilidade

---

## 🔄**elhorias Futuras

-**nclusão de novos contatos via**ntrada do usuário
- E**ção de contatos existentes
- Excl**ão de**egistros
- Persistência em arquiv** JSON
- Integração com banco de d**os
- Interface**ráfica com Tkinter
- API**EST utilizando Flask**u Django

---

## 👨‍💻**esenvolvedor

**André Filipe dos **ntos Reis**

Est**ante de Engenharia de Software co**foco em Desenvolvimento Back-end,**ython, Java e Segurança Cibernéti**.

GitHub: https://github.com/san**efilipedev

LinkedIn: https://lin**din.com/in/andrefilipedossantosre**

---

⭐ Projeto desenvolvido com** objetivo de consolidar**onhecimentos em Python e estrutur** de dados,**plicando conceitos fundamentais u**lizados no desenvolvimento de sof**are.
