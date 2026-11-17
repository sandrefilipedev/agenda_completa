# 📖 Contact Management System

## Overview

Contact Management System is a Python-based application designed to organize and manage personal and professional contact information through a command-line interface.

The application allows users to create, view, update, and delete contacts while supporting multiple communication methods such as phone numbers, email addresses, and physical addresses.

This project was developed to strengthen core software development skills and demonstrate practical application of Python data structures, modular programming, and data manipulation techniques.

---

## Project Goal

The primary goal of this project was to design a flexible and maintainable contact management solution using only native Python resources.

Throughout the development process, several fundamental software engineering concepts were applied, including data modeling, function decomposition, separation of concerns, and dynamic data handling.

---

## Business Problem

In real-world scenarios, a person often has multiple phone numbers, email addresses, or addresses that need to be organized and managed efficiently.

This project addresses that challenge by providing a structured and scalable solution capable of storing multiple contact methods for each individual while allowing easy maintenance and retrieval of information.

---

## Features

✅ Create new contacts

✅ Add multiple phone numbers per contact

✅ Add multiple email addresses per contact

✅ Store physical addresses

✅ Rename existing contacts

✅ Update contact information

✅ Delete contacts

✅ Display individual contact details

✅ Display the complete contact list

✅ Interactive command-line menu

---

## Technologies Used

- Python 3

---

## Technical Concepts Applied

### Data Structures

The application relies on Python's built-in data structures to organize information efficiently.

#### Tuples

Used to define the communication methods supported by the system.

```python
supported_contact_methods = (
    "phone",
    "email",
    "address"
)
```

#### Dictionaries

Used to store contacts and their associated information.

```python
contacts = {
    "John Doe": {
        "phone": [],
        "email": [],
        "address": []
    }
}
```

#### Lists

Used to store multiple values for the same contact method.

---

### Modular Programming

The application is organized into independent functions, each responsible for a specific task:

- Contact creation
- Contact deletion
- Contact updates
- Contact visualization
- Contact list management

This approach improves code readability, maintainability, and scalability.

---

### Dynamic Parameters

The project makes use of Python's `**kwargs` feature to handle multiple contact methods dynamically.

Example:

```python
def contact_to_text(contact_name, **contact_methods):
```

Thi**allows the system to remain flexi**e without requiring changes to th**function signature whenever** new contact method is introduced**
---

### CRUD**perations

The project implements**he four fundamental operations co**only found in real-world applicat**ns:

- Create
- Read
- Update
- D**ete

These operations are perform** entirely using native Python str**tures, simulating the behavior of** small**cale information management syste**

---

##**roject Structure

```text
agenda**ompleta/
│
├──**genda.py
├── README.md
└** .gitignore
```

---

## How to R**

Clone the repository:

```bash
**t clone https**/github.com/sandrefilip**ev/agenda_completa.git
```

Navig**e to the project folder:

```bash**d agenda_completa
```

**n the application:

```bash**ython agenda.py
```

---

## Exam**e**enu

```text
1 - Add contact
**- Add contact method
3 - Rename c**tact** - Update contact method
5 - Disp**y contact
6 - Display full contac**list
7** Delete contact
8 - Exit
```

---**## Skills Demonstrated

This proj**t demonstrates practical knowledg**of:

- Python Programming
- Data **ructures
- Dictionaries
- Lists
-**uples
- Functions
- CRUD Operatio**
- Modular Programming
- Dynamic **rameters (`**kwargs`)
- Data Mani**lation
- Software Design Fundamen**ls
- Problem Solving
- Code Organ**ation

---

## Future Enhancement**
Potential improvements for futur**versions include:

- JSON data pe**istence
- SQLite database integra**on
- Contact search functionality** Graphical User Interface (Tkinte**
- REST API development with Flas**- REST API development with Djang**- Authentication and authorizatio**features
- Cloud deployment

---
**# Key Learning Outcomes

Developi** this project reinforced importan**concepts related to Python progra**ing and software engineering fund**entals.

Beyond the technical imp**mentation, the project also provi**d hands-on experience in modeling**eal-world problems, designing mai**ainable solutions, and organizing**ode in a scalable manner.

---

#**Developer****André Filipe dos Santos Reis**
**oftware Engineering Student focus** on Backend Development, Python, **va, and Cybersecurity.

****tHub:** https://github.com**andrefilipedev

**LinkedIn:** htt**://linkedin.com/in/andrefilipedosantosreis

---

## Why This Projec**Matters

This project goes beyond** simple contact list application.**t demonstrates the ability to mod** data effectively, implement CRUD**perations, structure code using r**sable functions, and apply fundam**tal software development principl**.

It reflects practical experien** with**ython and showcases**kills that are directly**ransferable to larger**pplications involving databases, **Is,**nd enterprise systems.

⭐ Develop** as part of a continuous**earning journey in software devel**ment, with a focus on writing**lean, maintainable, and scalable **de.