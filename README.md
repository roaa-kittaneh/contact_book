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

  <img width="231" height="178" alt="Screenshot 2026-02-10 001855" src="https://github.com/user-attachments/assets/673e1b63-e054-4b90-9b52-469a73641861" />
  <img width="499" height="161" alt="Screenshot 2026-02-10 002239" src="https://github.com/user-attachments/assets/ac806e32-ec12-4d3e-b20d-b28da58ff742" />
  <img width="321" height="144" alt="Screenshot 2026-02-10 002001" src="https://github.com/user-attachments/assets/7d9cf3f3-894e-42ac-b77c-c8a2c5d2fb50" />
  <img width="304" height="149" alt="Screenshot 2026-02-10 002043" src="https://github.com/user-attachments/assets/2acfd74b-ec97-4c45-b67d-6c9742adcb95" />
  <img width="451" height="155" alt="Screenshot 2026-02-10 002049" src="https://github.com/user-attachments/assets/2e3d379e-c94a-4027-a38d-eca643bc579f" />
  <img width="235" height="156" alt="Screenshot 2026-02-10 002147" src="https://github.com/user-attachments/assets/52a4acd4-d25a-4f3e-adbe-82f544e9a504" />
  <img width="1010" height="129" alt="Screenshot 2026-02-10 003230" src="https://github.com/user-attachments/assets/661c175e-db8a-40ef-adfd-da7202588892" />








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
