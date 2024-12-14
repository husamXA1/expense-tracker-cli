from dataclasses import dataclass

@dataclass
class Expense:
  id: int
  description: str
  amount: int
  createdAt: int
  modifiedAt: int

if __name__ == "__main__":
  print("Welcome to expense tracker CLI")
