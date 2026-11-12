# 📒 Contact Management System

## Overview

Contact Management System is a Python application developed to organize and display personal and professional contact information in a structured and scalable way.

The project was built to reinforce core Python concepts such as data structures, functions, iteration, dynamic parameters, and data formatting while providing a practical solution for managing multiple contact methods for different people.

---

## Problem Statement

Managing contact information can become difficult when a single person has multiple phone numbers, email addresses, social media profiles, or physical addresses.

This project addresses that challenge by organizing contact information using nested dictionaries and lists, allowing multiple contact methods to be stored and displayed efficiently.

---

## Solution

The application stores contacts in a structured format and generates a formatted view of all contact information.

Each contact may contain:

- Phone numbers
- Email addresses
- Addresses
- LinkedIn profiles

The design allows easy expansion to support additional communication channels in the future.

---

## Key Features

- Store multiple contacts
- Support multiple phone numbers per contact
- Support multiple email addresses per contact
- LinkedIn profile management
- Structured data visualization
- Human-readable formatted output
- Extensible architecture

---

## Technologies Used

- Python 3

---

## Technical Concepts Applied

### Data Structures

The application leverages multiple Python data structures:

- Tuples
- Dictionaries
- Lists

Example:

```python
contatos_suportados = (
    "telefone",
    "email",
    "endereco",
    "linkedin"
)
```

### Nested Dictionaries

Contact information is stored using nested dictionaries:

```python
agenda = {
    "Pessoa 1": {
        "telefone": ["11 1234-5678"]
    }
}
```

### Functions

Business logic is separated into reusable functions:

```python
contato_para_texto()
agenda_para_texto()
```

### Dynamic Keyword Arguments

The project utilizes `**kwargs` to increase flexibility:

```python
def contato_para_texto(nome_contato, **formas_contato):
```

#****teration

Multiple loops are used**o process**nd format contact data dynamicall**

---

## Project Structure

```t**t
agenda-completa/
│
**─ agenda.py
└── README.md**``

---

## How to Run

Clone**he repository:

```bash
git clone**ttps://github.com/sandrefilipedev/agenda_completa.git
```

Navigate ** the project folder:

```bash
cd **enda_completa
```

Run the applic**ion:

```bash
python agenda.py
``**
---

## Sample Output

```text
P**soa 1

TE**FONE
    1 - 11**234-5678

EMAIL
    1 - pessoa@em**l.com
    **- email@profissional.com

ENDERE**
    1 - Rua 123

**NKEDIN
    1 - linkedin.com**n/pessoa1
```

---

## Skills**emonstrated

This project demonst**tes practical knowledge of**
- Python Fundamentals** Data Structures
- Functions** Dictionaries
- Lists
- Tu**es
- Nested Data Modeling** Iteration
- Dynamic**arameters (`**kwargs`)
- Code Organization** Problem Solving

---

##**uture Improvements

Planned enhan**ments include:

-**ontact creation through user inpu****Contact editing
- Contact removal** JSON persistence
- SQLite integr**ion** Search functionality
- Graphical**nterface (**inter)
- REST API implementation**sing Flask or Django

---

## Aut**r

****dré Filipe dos Santos Reis**

Sof**are Engineering Student focused o**Backend**evelopment, Python, Java, and Cyb**security.

- GitHub: https://**thub.com/sandrefilipedev
- Linked**: https://linkedin.com/in/andref**ipedossantosreis

---

###**hy This Project Matters

This pro**ct was developed to strengthen Py**on fundamentals and demonstrate p**ficiency in**rganizing, manipulating, and pres**ting**tructured data. It represents**n important step toward building **alable software**olutions using clean**nd maintainable code.
