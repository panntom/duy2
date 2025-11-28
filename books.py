"""
Books Management Module
Contributor 1's Implementation
"""


def generate_new_id(book_list):
    """Generate new ID for a book"""
    if not book_list:
        return 1
    else:
        max_id = max(book["id"] for book in book_list)
        return max_id + 1


def find_by_id(book_list, book_id):
    """Find a book by its ID"""
    for book in book_list:
        if book["id"] == book_id:
            return book
    return None


def add_book(books):
    """Add a new book to the library"""
    print("\n--- Add New Book ---")
    
    try:
        new_id = generate_new_id(books)
        
        title = input("Enter book title: ").strip()
        if not title:
            print("❌ Title cannot be empty!")
            return
        
        author = input("Enter author name: ").strip()
        if not author:
            print("❌ Author cannot be empty!")
            return
        
        year = input("Enter publication year: ").strip()
        if not year:
            print("❌ Year cannot be empty!")
            return
        
        new_book = {
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "status": "available"
        }
        
        books.append(new_book)
        
        print(f"✅ Book added successfully! ID: {new_id}")
        print(f"   Title: {title}")
        print(f"   Author: {author}")
        print(f"   Year: {year}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def list_books(books):
    """Display all books"""
    print("\n--- Book List ---")
    
    if not books:
        print("📚 No books in the library.")
        return
    
    print(f"Total books: {len(books)}\n")
    print(f"{'ID':<5} {'Title':<35} {'Author':<25} {'Year':<6} {'Status':<12}")
    print("-" * 90)
    
    for book in books:
        book_id = book.get("id", "N/A")
        title = book.get("title", "N/A")
        author = book.get("author", "N/A")
        year = book.get("year", "N/A")
        status = book.get("status", "N/A")
        
        if len(title) > 33:
            title = title[:30] + "..."
        if len(author) > 23:
            author = author[:20] + "..."
        
        print(f"{book_id:<5} {title:<35} {author:<25} {year:<6} {status:<12}")
    
    print()


def update_book(books):
    """Update book information"""
    print("\n--- Update Book ---")
    
    if not books:
        print("📚 No books in the library.")
        return
    
    try:
        book_id_str = input("Enter book ID to update: ").strip()
        if not book_id_str:
            print("❌ Book ID cannot be empty!")
            return
        
        try:
            book_id = int(book_id_str)
        except ValueError:
            print("❌ Book ID must be a number!")
            return
        
        book = find_by_id(books, book_id)
        if book is None:
            print(f"❌ Book ID {book_id} not found!")
            return
        
        print(f"\nCurrent information:")
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Year: {book['year']}")
        
        print("\nEnter new information (press Enter to keep current):")
        
        new_title = input(f"New title [{book['title']}]: ").strip()
        if new_title:
            book["title"] = new_title
        
        new_author = input(f"New author [{book['author']}]: ").strip()
        if new_author:
            book["author"] = new_author
        
        new_year = input(f"New year [{book['year']}]: ").strip()
        if new_year:
            book["year"] = new_year
        
        print(f"\n✅ Book ID {book_id} updated successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def delete_book(books):
    """Delete a book"""
    print("\n--- Delete Book ---")
    
    if not books:
        print("📚 No books in the library.")
        return
    
    try:
        book_id_str = input("Enter book ID to delete: ").strip()
        if not book_id_str:
            print("❌ Book ID cannot be empty!")
            return
        
        try:
            book_id = int(book_id_str)
        except ValueError:
            print("❌ Book ID must be a number!")
            return
        
        book = find_by_id(books, book_id)
        if book is None:
            print(f"❌ Book ID {book_id} not found!")
            return
        
        print(f"\nBook to delete:")
        print(f"  ID: {book['id']}")
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        
        confirm = input("\nAre you sure? (yes/no): ").strip().lower()
        
        if confirm == "yes" or confirm == "y":
            books.remove(book)
            print(f"✅ Book ID {book_id} deleted!")
        else:
            print("❌ Deletion cancelled.")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def books_menu(books):
    """Books management menu"""
    while True:
        print("\n" + "="*50)
        print("          BOOKS MANAGEMENT")
        print("="*50)
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter choice: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            add_book(books)
        elif choice == "2":
            list_books(books)
        elif choice == "3":
            update_book(books)
        elif choice == "4":
            delete_book(books)
        else:
            print("❌ Invalid choice. Choose 0-4.")
        
        input("\nPress Enter to continue...")