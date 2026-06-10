contacts = {}
while True:
        print("\n----Contact Manager----")
        print("1. Add contact")
        print("2. search contact")
        print("3. delete contact")
        print("4. Show contact")
        print("5. Exit")
        
        choice = int(input("Enter choice (1/2/3/4/5)"))
        if choice == 1:
            name = input("Enter contact name: ")
            phone = int(input("Enter conatct phone number: "))
            contacts[name]=phone
            
        elif choice ==2:
            name = input("Enter conatct name in search:")
            if name in contacts:
                print("Phone number: ", contacts[name])
            else:
                print("Contact not found.")
                
        elif choice == 3:
            name = input("Enter contact name to delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted.")
            else:
                print("Contact not found.")
                
        elif choice == 4:
            print("Contacts:")
            for name, phone in contacts.items():
                print("Name:", name, "Phone:", phone)
                break
        else:
            print("No contacts found.")