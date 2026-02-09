# Contact Book – Python Project

Simple Contact Book built with Python to practice real-world fundamentals:
functions, file handling, error handling, project structure, and testing.

## Features
- Add, view, update, and delete contacts
- Data persistence using `contacts.json`
- Safe file handling (missing / empty / corrupted JSON)
- Custom exception for strong password validation
- Unit tests using pytest
- Clean project structure (modules & packages)

## Project Structure
```
contact_book/
│── main.py
│── contacts.json
│
├── contacts/
│ ├── init.py
│ ├── manager.py
│ └── utils.py
│
└── tests/
├── conftest.py
└── test_contacts.py
```
