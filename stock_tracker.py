"""
CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker
The user enters stock names and quantities. Prices come from a hardcoded
dictionary. The program shows the total investment and can save it to a
.txt or .csv file.
"""

import csv

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130,
}


def show_available_stocks():
    """Print the list of stocks the user can choose from."""
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price}")
    print()


def get_quantity(symbol):
    """Keep asking until the user enters a positive whole number."""
    while True:
        text = input(f"Quantity of {symbol}: ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Please enter a whole number greater than 0.")


def collect_portfolio():
    """Ask the user for stocks and quantities. Return {symbol: quantity}."""
    portfolio = {}
    print("Enter a stock symbol and quantity. Type 'done' when finished.")

    while True:
        symbol = input("\nStock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            if portfolio:
                break
            print("Your portfolio is empty. Add at least one stock.")
            continue

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not available. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        quantity = get_quantity(symbol)
        # If the same stock is entered again, add to the old quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} x {symbol}.")

    return portfolio


def calculate_rows(portfolio):
    """Return a list of (symbol, quantity, price, value) and the total."""
    rows = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        rows.append((symbol, quantity, price, value))
        total += value
    return rows, total


def print_summary(rows, total):
    """Show the portfolio as a table."""
    print("\n" + "=" * 44)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * 44)
    for symbol, quantity, price, value in rows:
        print(f"{symbol:<8}{quantity:>6}{'$' + str(price):>10}{'$' + format(value, ','):>14}")
    print("-" * 44)
    print(f"{'Total investment:':<24}{'$' + format(total, ','):>20}")
    print("=" * 44)


def save_txt(rows, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio\n")
        f.write("-" * 40 + "\n")
        for symbol, quantity, price, value in rows:
            f.write(f"{symbol}: {quantity} x ${price} = ${value}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total investment: ${total}\n")
    return filename


def save_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    return filename


def ask_to_save(rows, total):
    """Optional: let the user save the result to a file."""
    answer = input("\nSave this result to a file? (y/n): ").strip().lower()
    if answer != "y":
        return

    while True:
        kind = input("Save as txt or csv? ").strip().lower()
        if kind in ("txt", "csv"):
            break
        print("Please type 'txt' or 'csv'.")

    try:
        filename = save_txt(rows, total) if kind == "txt" else save_csv(rows, total)
        print(f"Saved to {filename}")
    except OSError:
        print("Sorry, the file could not be saved.")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    show_available_stocks()

    portfolio = collect_portfolio()
    rows, total = calculate_rows(portfolio)
    print_summary(rows, total)
    ask_to_save(rows, total)
    print("\nThank you for using the tracker!")


if __name__ == "__main__":
    main()
