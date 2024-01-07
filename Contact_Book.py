def DisplayContactBook():
    print("Contact Book")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contact")
    print("4. Delete Contact")
    print("5. Exit")

def AddContact(contact):
    name = input("Enter the name:")
    phone = input("Enter the phone number:")
    contact[name] = phone
    print("Contact Added")

def SearchContact(contact):
    name = input("Enter the name to search:")
    if name in contact:
        print("Name:", name)
        print("Phone:", contact[name])
    else:
        print("Contact not found")

def DisplayContact(contact):
    if len(contact) == 0:
        print("Contact Book is empty")
    else:
        print("Contact Book")
        for name, phone in contact.items():
            print("Name:", name)
            print("Phone:", phone)

def DeleteContact(contact):
    name = input("Enter the name to delete:")
    if name in contact:
        del contact[name]
        print("Contact deleted")
    else:
        print("Contact not found")

def Exit():
    print("Thanks for using Contact Book")
    exit()

contact = {}
while True:
    DisplayContactBook()
    choice = int(input("Enter your choice:"))

    if choice == 1:
        AddContact(contact)
    elif choice == 2:
        SearchContact(contact)
    elif choice == 3:
        DisplayContact(contact)
    elif choice == 4:
        DeleteContact(contact)
    elif choice == 5:
        Exit()
    else:
        print("Invalid Choice")
