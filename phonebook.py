import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully")

def view_contacts():
    contacts = load_contacts()
    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("")

def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ")
    for contact in contacts:
        if name == contact["name"]:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            break
    else:
        print("No contact found")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ")
    new_contacts = [contact for contact in contacts if name != contact["name"]]
    if len(contacts) != len(new_contacts):
        save_contacts(new_contacts)
        print("Contact deleted successfully")
    else:
        print("No contact found")

def main():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()