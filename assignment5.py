import csv
import os

# Define the file name globally so we can easily change it if needed
FILE_NAME = 'expenses.csv'

def init_file():
    """Initializes the CSV file with headers if it does not already exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Note'])

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter Date (e.g., YYYY-MM-DD): ")
    category = input("Enter Category (e.g., Food, Travel, Utilities): ").title()
    
    # Exception handling for the amount input
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break # Exit the loop if input is valid
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value for the amount.")
            
    note = input("Enter Note (optional, press Enter to skip): ")

    # File handling to append data
    try:
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])
        print("✅ Expense added successfully!")
    except Exception as e:
        print(f"❌ Error saving expense: {e}")

def view_expenses():
    print("\n--- All Recorded Expenses ---")
    total_amount = 0.0
    
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            records = list(reader)
            
            if not records:
                print("No expenses recorded yet.")
                return
            
            # Formatting the output into a clean table
            print(f"{'Date':<15} | {'Category':<15} | {'Amount':<10} | {'Note'}")
            print("-" * 60)
            
            for row in records:
                amount = float(row['Amount'])
                total_amount += amount
                print(f"{row['Date']:<15} | {row['Category']:<15} | ${amount:<9.2f} | {row['Note']}")
                
            print("-" * 60)
            print(f"💰 Total Amount Spent: ${total_amount:.2f}")
            
    except FileNotFoundError:
        print("❌ No expense file found. Please add an expense first.")
    except Exception as e:
        print(f"❌ Error reading expenses: {e}")

def category_summary():
    print("\n--- Category-wise Spending Summary ---")
    category_totals = {}
    
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Aggregate amounts by category
            for row in reader:
                category = row['Category']
                amount = float(row['Amount'])
                
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
                    
            if not category_totals:
                print("No expenses recorded yet.")
                return
            
            print(f"{'Category':<20} | {'Total Spent'}")
            print("-" * 40)
            for category, total in category_totals.items():
                print(f"{category:<20} | ${total:.2f}")
                
    except FileNotFoundError:
        print("❌ No expense file found. Please add an expense first.")
    except Exception as e:
        print(f"❌ Error reading expenses: {e}")

def main():
    init_file() # Ensure the CSV is ready when the program starts
    
    while True:
        print("\n" + "="*35)
        print(" 📊 Expense Tracker Menu 📊")
        print("="*35)
        print("1. Add New Expense")
        print("2. View All Expenses & Total")
        print("3. View Category-wise Summary")
        print("4. Exit")
        print("="*35)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
