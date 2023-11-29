'''Date:22 november 2023
Author:Mahendra pratap singh
Programme: Contact book.'''
import os
#defining add contact function
def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    with open("contacts.txt", "a") as contacts_file:
        contacts_file.write(f"{name}: {phone_number}, {email}, {address}\n")
#defining view function
def view_contacts():
    with open("contacts.txt", "r") as contacts_file:
        contacts = contacts_file.read().splitlines()
        for contact in contacts:
            print(contact)
#search contact
def search_contact():
    search_term = input("Enter name or phone number to search for: ")
    with open("contacts.txt", "r") as contacts_file:
        contacts = contacts_file.read().splitlines()
        found_contacts = []
        for contact in contacts:
            if search_term in contact:
                found_contacts.append(contact)
        if found_contacts:
            print("Found contacts:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found matching the search term.")
#for updating contact
def update_contact():
    contact_name = input("Enter contact name to update: ")
    with open("contacts.txt", "r") as contacts_file:
        contacts = contacts_file.read().splitlines()
#taking updated matters
    for contact in contacts:
        if contact.startswith(contact_name):
            updated_name = input("Enter updated name: ")
            updated_phone_number = input("Enter updated phone number: ")
            updated_email = input("Enter updated email: ")
            updated_address = input("Enter updated address: ")
            updated_contact = f"{updated_name}: {updated_phone_number}, {updated_email}, {updated_address}"
            contacts.remove(contact)
            contacts.append(updated_contact)
            with open("contacts.txt", "w") as contacts_file:
                contacts_file.write("\n".join(contacts))
            break
#for deleting contact
def delete_contact():
    contact_name = input("Enter contact name to delete: ")
    with open("contacts.txt", "r") as contacts_file:
        contacts = contacts_file.read().splitlines()
    for contact in contacts:
        if contact.startswith(contact_name):
            contacts.remove(contact)
            with open("contacts.txt", "w") as contacts_file:
                contacts_file.write("\n".join(contacts))
            break
#now viewing contact list menu
def main():
    choice = input("""
        Contact List Menu:

        1. Add Contact
        2. View Contact List
        3. Search Contact
        4. Update Contact
        5. Delete Contact
        6. Exit
        
        Enter your choice: """)
#taking user choice
    while choice != "6":
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        else:
            print("Invalid choice. Please try again.")
        choice = input("\nEnter your choice: ")
    print("Goodbye!")
if __name__ == "_main_":
       main() 