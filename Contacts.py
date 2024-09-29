import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
           
            for contact in contacts:
                if 'category' not in contact:
                    contact['category'] = 'unknown'  
            return contacts
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact(contacts):
    first_name = input("Enter contact's first name: ")
    last_name = input("Enter contact's last name: ")
    full_name = f"{first_name} {last_name}"

    phone = input("Enter phone number (10 digits): ")
    while not validate_phone(phone):
        print("Invalid phone number. Please enter a valid 10-digit phone number.")
        phone = input("Enter phone number (10 digits): ")

    email = input("Enter email address: ")

    category = ""
    while category.lower() not in ['work', 'home']:
        category = input("Enter contact category (work/home): ").lower()

    contact = {"name": full_name, "phone": phone, "email": email, "category": category}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {full_name} ({category}) added successfully.")

def view_contacts(contacts):
    if contacts:
        for idx, contact in enumerate(contacts, start=1):
            # Provide defaults if any field is missing
            name = contact.get('name', 'Unknown Name')
            phone = contact.get('phone', 'Unknown Phone')
            email = contact.get('email', 'Unknown Email')
            category = contact.get('category', 'Unknown').capitalize()

            print(f"{idx}. {name} | {phone} | {email} | {category}")
    else:
        print("Contact list is empty.")

def edit_contact(contacts):
    view_contacts(contacts)
    contact_index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= contact_index < len(contacts):
        contact = contacts[contact_index]
        print(f"Editing {contact['name']}")
        
        first_name = input(f"Enter new first name ({contact['name'].split()[0]}): ") or contact['name'].split()[0]
        last_name = input(f"Enter new last name ({contact['name'].split()[1]}): ") or contact['name'].split()[1]
        contact['name'] = f"{first_name} {last_name}"
        
        phone = input(f"Enter new phone number ({contact['phone']}, 10 digits): ") or contact['phone']
        while not validate_phone(phone):
            print("Invalid phone number. Please enter a valid 10-digit phone number.")
            phone = input(f"Enter new phone number ({contact['phone']}, 10 digits): ")
        contact['phone'] = phone

        contact['email'] = input(f"Enter new email address ({contact['email']}): ") or contact['email']

        category = ""
        while category.lower() not in ['work', 'home']:
            category = input(f"Enter new contact category ({contact['category']}): ").lower() or contact['category']
        contact['category'] = category
        
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    view_contacts(contacts)
    contact_index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= contact_index < len(contacts):
        contact = contacts.pop(contact_index)
        save_contacts(contacts)
        print(f"Contact {contact['name']} deleted successfully.")
    else:
        print("Invalid contact number.")

def search_contact(contacts):
    search_term = input("Enter the name or phone number to search for: ").lower()
    
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term == contact['phone']]
    
    if results:
        print("\nSearch Results:")
        for idx, contact in enumerate(results, start=1):
            name = contact.get('name', 'Unknown Name')
            phone = contact.get('phone', 'Unknown Phone')
            email = contact.get('email', 'Unknown Email')
            category = contact.get('category', 'Unknown').capitalize()

            print(f"{idx}. {name} | {phone} | {email} | {category}")
    else:
        print("No contacts found matching the search term.")

# Main menu
def menu():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
