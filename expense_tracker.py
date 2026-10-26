import argparse, json
from collections import defaultdict
from datetime import date
from pathlib import Path

DB = Path("expenses.json")

def load():
    return json.loads(DB.read_text()) if DB.exists() else []

def add(args):
    data = load()
    data.append({"date": str(date.today()), "amount": args.amount,
                 "category": args.category, "note": args.note})
    DB.write_text(json.dumps(data, indent=2))
    print(f"Added ₹{args.amount:.2f} to {args.category}")

def report(_):
    data = load()
    if not data:
        return print("No expenses yet.")
    totals = defaultdict(float)
    for e in data:
        totals[e["category"]] += e["amount"]
    top = max(totals.values())
    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{cat:<12} ₹{amt:>9.2f} {'█' * int(amt / top * 30)}")
    print(f"\nTotal: ₹{sum(totals.values()):.2f}")

p = argparse.ArgumentParser(description="Tiny expense tracker")
sub = p.add_subparsers(required=True)
a = sub.add_parser("add")
a.add_argument("amount", type=float)
a.add_argument("category")
a.add_argument("note", nargs="?", default="")
a.set_defaults(fn=add)
sub.add_parser("report").set_defaults(fn=report)
args = p.parse_args()
args.fn(args)