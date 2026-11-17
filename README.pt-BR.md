# 📖 Agenda de Contatos em Python

## Visão Geral

Este projeto consiste em uma aplicação desenvolvida em Python para gerenciamento de contatos através do terminal.

A aplicação permite cadastrar, consultar, atualizar e remover contatos, além de gerenciar diferentes formas de comunicação, como telefone, e-mail e endereço.

O objetivo principal do projeto foi aplicar conceitos fundamentais de programação, estruturas de dados e organização de código, simulando funcionalidades encontradas em sistemas reais de gerenciamento de informações.

---

## Objetivo do Projeto

Desenvolver uma solução simples e funcional para gerenciamento de contatos, utilizando apenas recursos nativos da linguagem Python.

Durante o desenvolvimento foram explorados conceitos importantes da engenharia de software, como modelagem de dados, reutilização de código, separação de responsabilidades e manipulação dinâmica de informações.

---

## Problema Resolvido

Na rotina pessoal e profissional, é comum que uma pessoa possua mais de um telefone, e-mail ou endereço.

O projeto resolve esse cenário através de uma estrutura flexível que permite armazenar múltiplas formas de contato para cada pessoa, possibilitando consulta, atualização e exclusão de informações de maneira organizada.

---

## Funcionalidades

✅ Cadastro de novos contatos

✅ Inclusão de múltiplos telefones por contato

✅ Inclusão de múltiplos e-mails por contato

✅ Inclusão de endereços

✅ Alteração do nome do contato

✅ Atualização de informações existentes

✅ Exclusão de contatos

✅ Consulta individual de contatos

✅ Exibição de toda a agenda formatada

✅ Menu interativo via terminal

---

## Tecnologias Utilizadas

- Python 3

---

## Conceitos Aplicados

### Estruturas de Dados

O projeto utiliza estruturas nativas do Python para armazenar e organizar informações.

#### Tuplas

Utilizadas para definir os tipos de contato suportados pelo sistema.

```python
contatos_suportados = (
    "telefone",
    "email",
    "endereco"
)
```

#### Dicionários

Responsáveis pelo armazenamento dos contatos e suas informações.

```python
agenda = {
    "Nome": {
        "telefone": [],
        "email": [],
        "endereco": []
    }
}
```

#### Listas

Utilizadas para armazenar múltiplos valores para uma mesma forma de contato.

---

### Programação Funcional

O sistema foi dividido em funções específicas para cada responsabilidade:

- Inclusão de contatos
- Exclusão de contatos
- Alteração de dados
- Visualização de informações
- Manipulação da agenda

Essa abordagem facilita a manutenção e aumenta a legibilidade do código.

---

### Parâmetros Dinâmicos

Foi utilizada a estratégia de parâmetros dinâmicos com `**kwargs`, permitindo trabalhar com diferentes formas de contato sem necessidade de alterar a estrutura das funções.

Exemplo:

```python
def contato_para_texto(nome_contato, **formas_contato):
```

---

### Ma**pulação de Dados

**projeto realiza operações complet** de**
- Criação
- Leitura
-**tualização
- Exclusão

Caracter**ando uma implementação prática do**onceito CRUD.

---

## Estrutura ** Projeto

```text
agenda-completa**│
├** agenda.py
├── README.md
└── .git**nore
```

---

## Como Executar

**one o repositório:

**`bash
git clone https://github.com/sandrefilipedev/agenda_completa.git
```

Acesse a pasta do projeto**
```bash
cd agenda_completa
``**
Execute o programa:

```bash
pyt**n agenda**y
```

---

## Exemplo de Util**ação

```text
1 - In**uir contato na agenda
2 - Incluir**ma forma de contato
3 - Alterar o**ome de um contato
4 - Alterar uma**orma**e contato
5 - Exibir um contato
**- Exibir toda a agenda
7 -**xcluir um contato
8 - Sair
**`

---

## Competências Demonstra**s

Este**rojeto evidencia conhecimentos em**
- Python
- Estruturas de Dados
**Dicionários
- Tu**as
- Listas
- Funções
**CRUD
- Manipulação de**ados
- Lógica de Programação
**Tratamento de Flux**- Organização de Código** Resolução de Problemas

---

## **ssíveis Evoluções**Como próximos**assos, o projeto pode ser**xpandido para incluir:

- Persist**cia de dados em JSON
- Integração**om SQLite
- Interface gráfica com**kinter
- API REST com Flask
- API**EST com Django
- Sistema de auten**cação
- Busca inteligente de cont**os

---

## Aprendizados

Durante** desenvolvimento deste projeto fo**possível consolidar conhecimentos**m estruturas de dados, modulariza**o de código e manipulação dinâmic**de informações utilizando Python.**Além do aspecto técnico, o projet**contribuiu para o desenvolvimento**a capacidade de modelar problemas**eais e transformá-los em soluções**e software organizadas e reutiliz**eis.

---

## Desenvolvedor

**An**é Filipe dos Santos Reis**

Estud**te de Engenharia de Software com **co em Desenvolvimento Back-end, P**hon, Java e Segurança Cibernética**
**GitHub:** https://github.com/s**drefilipedev

**LinkedIn:** https**/linkedin.com/in/andrefilipedossa**osreis

---

⭐ Este projeto foi d**envolvido com o objetivo de forta**cer fundamentos de desenvolviment**de software e demonstrar a aplica**o prática de estruturas de dados **lógica de programação na construç** de uma solução funcional para ge**nciamento de contatos.