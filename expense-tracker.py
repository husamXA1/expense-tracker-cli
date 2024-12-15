from dataclasses import dataclass
import sys

@dataclass
class Expense:
  id: int
  description: str
  amount: int
  createdAt: int
  modifiedAt: int

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
