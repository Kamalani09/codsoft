contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact for {name} added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("\nEnter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    keyword = input("\nEnter name or phone to update: ").lower()
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print(f"\nUpdating contact for {contact['name']}")
            contact['name'] = input("New Name: ") or contact['name']
            contact['phone'] = input("New Phone: ") or contact['phone']
            contact['email'] = input("New Email: ") or contact['email']
            contact['address'] = input("New Address: ") or contact['address']
            print("Contact updated successfully.")
            return
    print("No matching contact found.")

def delete_contact():
    keyword = input("\nEnter name or phone to delete: ").lower()
    for i, contact in enumerate(contacts):
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                print("Contact deleted successfully.")
            else:
                print("Deletion cancelled.")
            return
    print("No matching contact found.")

def main():
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

# Run the program
main()

