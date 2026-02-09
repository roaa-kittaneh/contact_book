from contacts.manager import (
    add_contact,
    delete_contact,
    update_contact,
    load_contacts
)


def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            country = input("Country (default PS): ") or "PS"
            add_contact(name, phone, country)
            print("✅ Contact added")

        elif choice == "2":
            contacts = load_contacts()
            if not contacts:
                print("No contacts found")
            for c in contacts:
                print(c)

        elif choice == "3":
            phone = input("Phone to update: ")
            new_name = input("New name (leave empty to skip): ")
            new_country = input("New country (leave empty to skip): ")

            updated = update_contact(
                phone,
                new_name or None,
                new_country or None
            )

            if updated:
                print("✅ Contact updated")
            else:
                print("❌ Contact not found")

        elif choice == "4":
            phone = input("Phone to delete: ")
            deleted = delete_contact(phone)

            if deleted:
                print("🗑 Contact deleted")
            else:
                print("❌ Contact not found")

        elif choice == "5":
            print("Bye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
