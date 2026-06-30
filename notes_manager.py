notes=[]

def menu():
    print("\n--- NOTE MANAGER ---")
    print("1. List notes")
    print("2. Add note")
    print("3. Save notes")
    print("4. Load notes")
    print("5. Exit")

def add_note():
    note=input("Enter a note:")

    if not note:
        print("note cannot be empty")
        return
    notes.append(note)
    print("Note added sucessfully")

def view_notes():
    if not notes:
        print("No notes found")
        return
    
    for i, note in enumerate(notes, start=1):
        print(f"{i}.{note}")

def save_notes():
    file=open("notes.txt","w")

    for note in notes:
        file.write(note+"\n")
    file.close()

    print("Notes saved successfully")
def load_notes():

    try:
        file=open("notes.txt","r")

        notes.clear()

        for line in file:
            notes.append(line.strip())

        file.close()

        print("Notes loaded successfully")

    except FileNotFoundError:
        print("No saved notes found")

while True:
    menu()
    option=input("Choose an option: ")

    if option=="1":
        view_notes()

    elif option=="2":
        add_note()

    elif option=="3":
        save_notes()

    elif option=="4":
        load_notes()

    elif option=="5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
