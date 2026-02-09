from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)
FILE_NAME = "expenses.csv"

@app.route("/")
def home():
    expenses = []
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
                total += float(row[2])
    except:
        pass
    return render_template("index.html", expenses=expenses, total=total)

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
