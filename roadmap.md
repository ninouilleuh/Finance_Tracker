# 💰 Finance Tracker Roadmap

## Current Version (v1.0)

### ✅ Completed

- Add new expenses
- Delete expenses with confirmation
- Load previous expenses
- Save expenses automatically
- Input validation
- Error handling
- Statistics by category
- Total amount spent
- Highest spending category
- Menu-driven interface
- Refactored code with reusable functions
- Centralized file loading and saving

---

# 🚀 Next Features

## 1. Edit an Expense

**Priority:** High

Allow the user to modify an existing expense instead of deleting it.

The user should be able to edit:

- Category
- Amount

Example:

```
Expense #3

Current category: Food
Current amount: 15

New category:
New amount:
```

---

## 2. Expense Dates

**Priority:** High

Store the date for every expense.

Current format:

```
Food | 20
```

New format:

```
2026-07-19 | Food | 20
```

This prepares the project for monthly reports and searching by date.

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

## 4. Monthly Reports

**Priority:** Medium

Generate spending summaries by month.

Example:

```
July 2026

Food: 120
Transport: 42
Games: 60

Total: 222
```

---

## 5. Income & Balance

**Priority:** High

Track income in addition to expenses.

The application should display:

- Total income
- Total expenses
- Current balance

---

## 6. Savings Goal

**Priority:** Medium

Set a savings goal.

Example:

```
Goal: €15,000

Saved: €3,200

Progress

████░░░░░░░░░░░░░ 21%
```

---

# 🌱 Future Features

- Debt tracker
- Settings menu
- JSON storage
- SQLite database
- Export reports (CSV)
- Currency conversion (EUR ⇄ JPY)
- ASCII charts
- Multiple user profiles
- Budget limits and alerts
- Recurring expenses

---

# 🎯 Long-Term Goal

Transform this project from a beginner Python application into a polished command-line finance tracker.

The project should demonstrate:

- Clean code
- Modular architecture
- Input validation
- File handling
- Data processing
- Software design
- Refactoring
- Version control with Git
