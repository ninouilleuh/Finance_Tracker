# Finance Tracker Roadmap

## Current Version (v0.1)

### ✅ Completed

* Add new expense
* Save expenses to a file
* Load previous expenses
* Input validation
* Statistics by category
* Total spent
* Highest spending category
* Menu system

---

# Next Features

## 1. Delete an Expense

**Priority:** High

Allow the user to:

* View all expenses with numbers.
* Select one to delete.
* Save the updated list.

Example:

```
1. Food | 20
2. Games | 50
3. Rent | 800

Choose an expense to delete:
```

---

## 2. Edit an Expense

**Priority:** High

Instead of deleting an incorrect expense, allow the user to edit:

* Category
* Amount

Example:

```
Expense #3

Current category: Food
Current amount: 15

New category:
New amount:
```

---

## 3. Search Expenses

**Priority:** Medium

Search by category.

Example:

```
Search:

Food
```

Output:

```
Food | 15
Food | 32
Food | 9

Total: 56
```

---

## 4. Income & Balance

**Priority:** High

Add income tracking.

Menu:

```
1. Add income
2. Add expense
```

The application should display:

* Total income
* Total expenses
* Current balance

---

## 5. Savings Goal

**Priority:** Medium

Set a savings goal.

Example:

```
Goal: €15,000

Saved: €3,200

Progress:

████░░░░░░░░░░░░░ 21%
```

This feature is intended to help track progress toward moving to Japan.

---

# Future Features

* Monthly reports
* Expense dates
* Debt tracker
* JSON storage
* Settings menu
* Export reports
* Currency conversion (EUR ⇄ JPY)
* ASCII charts
* Multiple user profiles

---

# Long-Term Goal

Transform this project from a beginner Python exercise into a polished command-line finance application suitable for a GitHub portfolio.

The project should demonstrate:

* Clean code
* Modular architecture
* Input validation
* File handling
* Data processing
* Software design
* Git version history
