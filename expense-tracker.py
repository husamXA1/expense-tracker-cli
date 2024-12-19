from dataclasses import dataclass
import sys, time

@dataclass
class Expense:
  id: int
  description: str
  amount: int
  createdAt: int
  modifiedAt: int

def load_expenses():
  # TODO: load expenses from data.json
  return []

def save_expenses(expenses):
  # TODO: save expenses to data.json
  pass

def get_latest_id():
    # TODO: read last id from data.json
    return 1

def add_expense(description, amount):
  expenses = load_expenses()
  expense = Expense(
                id=get_latest_id(),
                description=description, 
                amount=amount,
                createdAt=time.time(),
                modifiedAt=time.time()
            )
  expenses.append(expense)
  save_expenses(expenses)

def delete_expense(id):
  expenses = load_expenses()
  for expense in expenses:
    if expense.id == id:
      expenses.remove(expense)
  save_expenses(expenses)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("USAGE: expense-tracker [COMMAND]")
    sys.exit(1)
  match sys.argv[1]:
    case "add":
        print("adding expense")
    case "list":
        print("listing expenses")
    case "summary":
        print("printing summary")
    case "delete":
        print("deleting an expense")
    case _:
      print("invalid command!")
      sys.exit(1)
