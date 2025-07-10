contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("✅ Contact added successfully!\n")

def view_contacts():
    if len(contacts) == 0:
        print("📭 No contacts to show.\n")
    else:
        print("📇 Contact List:")
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()

def delete_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    try:
        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(contacts):
            removed = contacts.pop(choice - 1)
            print(f"🗑️ Contact '{removed['name']}' deleted.\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main():
    while True:
        print("📱 Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1 and 4.\n")

if __name__ == "__main__":
    main()
