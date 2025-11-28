"""
Smart Campus Library System
Team Leader Implementation
Main program structure with menu and data handling
"""

import json
import os
from books import books_menu as books_management_menu

# Constants - File paths
BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"
LOANS_FILE = "data/loans.json"

# Global data structures
books = []
members = []
loans = []


def load_data():
    """
    Load data from JSON files into global lists
    Team Leader's responsibility
    """
    global books, members, loans
    
    try:
        # Load books
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
                books = json.load(f)
            print(f"✅ Loaded {len(books)} books")
        else:
            books = []
            print("⚠️ No books.json found, starting with empty list")
        
        # Load members
        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE, 'r', encoding='utf-8') as f:
                members = json.load(f)
            print(f"✅ Loaded {len(members)} members")
        else:
            members = []
            print("⚠️ No members.json found, starting with empty list")
        
        # Load loans
        if os.path.exists(LOANS_FILE):
            with open(LOANS_FILE, 'r', encoding='utf-8') as f:
                loans = json.load(f)
            print(f"✅ Loaded {len(loans)} loans")
        else:
            loans = []
            print("⚠️ No loans.json found, starting with empty list")
            
    except json.JSONDecodeError as e:
        print(f"❌ Error loading JSON: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def save_data():
    """
    Save all data to JSON files
    Team Leader's responsibility
    """
    global books, members, loans
    
    try:
        # Create data directory if not exists
        os.makedirs("data", exist_ok=True)
        
        # Save books
        with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=2, ensure_ascii=False)
        
        # Save members
        with open(MEMBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(members, f, indent=2, ensure_ascii=False)
        
        # Save loans
        with open(LOANS_FILE, 'w', encoding='utf-8') as f:
            json.dump(loans, f, indent=2, ensure_ascii=False)
        
        print("💾 Data saved successfully!")
        
    except Exception as e:
        print(f"❌ Error saving data: {e}")


def display_main_menu():
    """
    Display the main menu
    Team Leader's responsibility
    """
    print("\n" + "="*50)
    print("     Smart Campus Library System")
    print("="*50)
    print("1. Books")
    print("2. Members")
    print("3. Loans")
    print("4. Overdue Report")
    print("0. Exit")
    print("="*50)


def books_menu():
    """Books menu - IMPLEMENTED BY CONTRIBUTOR 1"""
    global books
    books_management_menu(books)


def members_menu():
    """
    Members management submenu
    TO BE IMPLEMENTED BY CONTRIBUTOR 2
    """
    print("\n--- Members Management ---")
    print("⚠️ This feature will be implemented by Contributor 2")
    print("Waiting for feature/members-loans branch...")
    input("\nPress Enter to continue...")


def loans_menu():
    """
    Loans management submenu
    TO BE IMPLEMENTED BY CONTRIBUTOR 2
    """
    print("\n--- Loans Management ---")
    print("⚠️ This feature will be implemented by Contributor 2")
    print("Waiting for feature/members-loans branch...")
    input("\nPress Enter to continue...")


def overdue_report():
    """
    Generate overdue report
    TO BE IMPLEMENTED BY CONTRIBUTOR 2
    """
    print("\n--- Overdue Report ---")
    print("⚠️ This feature will be implemented by Contributor 2")
    print("Waiting for feature/members-loans branch...")
    input("\nPress Enter to continue...")


def main():
    """
    Main program loop
    Team Leader's responsibility
    """
    print("🚀 Starting Smart Campus Library System...")
    
    # Load data at startup
    load_data()
    
    # Main loop
    while True:
        display_main_menu()
        main_choice = input("Enter choice: ").strip()
        
        if main_choice == "0":
            # Exit program
            save_data()
            print("\n👋 Goodbye! Thank you for using our system.")
            break
        
        elif main_choice == "1":
            # Books Management - Contributor 1's work
            books_menu()
        
        elif main_choice == "2":
            # Members Management - Contributor 2's work
            members_menu()
        
        elif main_choice == "3":
            # Loans Management - Contributor 2's work
            loans_menu()
        
        elif main_choice == "4":
            # Overdue Report - Contributor 2's work
            overdue_report()
        
        else:
            print("❌ Invalid option. Please choose 0-4.")
        
        # Save data after each operation
        save_data()


if __name__ == "__main__":
    main()