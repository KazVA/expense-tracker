# Expense Tracker

A simple Python CLI app to record expenses and view category totals as a text bar chart.

## Requirements
- Python 3

## Usage
```bash
python expense_tracker.py add 250 food "lunch"
python expense_tracker.py report
```

## Example Output
```text
Added ₹250.00 to food

food          ₹   250.00 ██████████████████████████████

Total: ₹250.00
```

Expenses are saved locally in `expenses.json`.