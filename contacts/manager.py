import json
from pathlib import Path

FILE_PATH = Path("contacts.json")


def load_contacts():
    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_contacts(contacts):
    with open(FILE_PATH, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(name, phone, country="PS"):
    contacts = load_contacts()

    contact = {
        "name": name,
        "phone": phone,
        "country": country
    }

    contacts.append(contact)
    save_contacts(contacts)
    return contact


def delete_contact(phone):
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["phone"] != phone]

    save_contacts(updated_contacts)
    return len(contacts) != len(updated_contacts)


def update_contact(phone, new_name=None, new_country=None):
    contacts = load_contacts()

    for contact in contacts:
        if contact["phone"] == phone:
            if new_name:
                contact["name"] = new_name
            if new_country:
                contact["country"] = new_country

            save_contacts(contacts)
            return True

    return False
