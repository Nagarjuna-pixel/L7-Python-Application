from database import initialize_database
from app import display_flavors, add_new_flavor

def main():
    initialize_database()
    print("Welcome to Ice Cream Parlor!")
    while True:
        print("\n1. Display Flavors")
        print("2. Add New Flavor")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_flavors()
        elif choice == "2":
            add_new_flavor()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
