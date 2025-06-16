# Define your stock portfolio
portfolio = {
    'AAPL': {'shares': 10, 'price': 190.50},
    'GOOGL': {'shares': 5, 'price': 2800.00},
    'TSLA': {'shares': 8, 'price': 185.25},
    'AMZN': {'shares': 2, 'price': 3300.75},
}

# Calculate total investment
def calculate_total_investment(portfolio):
    total = 0
    print("Your Stock Portfolio Summary:\n")
    for stock, data in portfolio.items():
        shares = data['shares']
        price = data['price']
        value = shares * price
        total += value
        print(f"{stock}: {shares} shares @ ${price:.2f} = ${value:.2f}")
    print(f"\nTotal Investment Value: ${total:.2f}")
    return total

# Run the calculation
calculate_total_investment(portfolio)
