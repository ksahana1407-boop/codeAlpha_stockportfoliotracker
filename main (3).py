
# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0

print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        investment = stock_prices[stock] * quantity
        print(f"{stock} investment = {stock_prices[stock]} × {quantity} = ₹{investment}")

        total_investment = total_investment + investment
    else:
        print("Stock not found! Please try again.")

print("\nTotal Investment Value: ₹", total_investment)