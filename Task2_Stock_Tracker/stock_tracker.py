import csv
from datetime import datetime
import os

def stock_tracker():
    """
    Simple Stock Tracker
    Calculates total investment based on hardcoded stock prices.
    """
    
    # Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180.50,    # Apple Inc.
        "TSLA": 250.75,    # Tesla Inc.
        "GOOGL": 135.20,   # Alphabet Inc.
        "MSFT": 340.80,    # Microsoft Corporation
        "AMZN": 145.30,    # Amazon.com Inc.
        "NVDA": 485.60,    # NVIDIA Corporation
        "META": 325.15,    # Meta Platforms Inc.
        "NFLX": 445.90,    # Netflix Inc.
        "PYPL": 58.25,     # PayPal Holdings Inc.
        "AMD": 115.40      # Advanced Micro Devices
    }
    
    print("📈 STOCK INVESTMENT TRACKER 📈")
    print("=" * 50)
    print("Available stocks and their current prices:")
    print("-" * 50)
    
    # Display available stocks
    for symbol, price in stock_prices.items():
        print(f"{symbol:<8} ${price:>8.2f}")
    
    print("-" * 50)
    
    # Store user's portfolio
    portfolio = []
    total_investment = 0
    
    while True:
        print(f"\nCurrent total investment: ${total_investment:.2f}")
        print("\nOptions:")
        print("1. Add stock to portfolio")
        print("2. View portfolio summary")
        print("3. Save portfolio to file")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Add stock to portfolio
            stock_symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
            
            if stock_symbol not in stock_prices:
                print(f"❌ Stock symbol '{stock_symbol}' not found in our database.")
                print(f"Available symbols: {', '.join(stock_prices.keys())}")
                continue
            
            try:
                quantity = float(input(f"Enter quantity for {stock_symbol}: "))
                if quantity <= 0:
                    print("❌ Quantity must be greater than 0.")
                    continue
                
                stock_price = stock_prices[stock_symbol]
                investment_value = quantity * stock_price
                
                # Add to portfolio
                portfolio.append({
                    'symbol': stock_symbol,
                    'quantity': quantity,
                    'price': stock_price,
                    'value': investment_value
                })
                
                total_investment += investment_value
                
                print(f"✅ Added {quantity} shares of {stock_symbol} at ${stock_price:.2f} each")
                print(f"Investment value: ${investment_value:.2f}")
                
            except ValueError:
                print("❌ Please enter a valid number for quantity.")
        
        elif choice == '2':
            # View portfolio summary
            display_portfolio_summary(portfolio, total_investment)
        
        elif choice == '3':
            # Save portfolio to file
            if not portfolio:
                print("❌ No stocks in portfolio to save.")
            else:
                save_portfolio(portfolio, total_investment)
        
        elif choice == '4':
            print("Thank you for using Stock Investment Tracker! 📊")
            break
        
        else:
            print("❌ Invalid choice. Please select 1-4.")

def display_portfolio_summary(portfolio, total_investment):
    """
    Display detailed portfolio summary
    """
    if not portfolio:
        print("\n📋 Portfolio is empty.")
        return
    
    print(f"\n📋 PORTFOLIO SUMMARY")
    print("=" * 60)
    print(f"{'Symbol':<8} {'Quantity':<10} {'Price':<10} {'Value':<12}")
    print("-" * 60)
    
    for stock in portfolio:
        print(f"{stock['symbol']:<8} {stock['quantity']:<10.2f} ${stock['price']:<9.2f} ${stock['value']:<11.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL INVESTMENT:':<38} ${total_investment:.2f}")
    print("=" * 60)

def save_portfolio(portfolio, total_investment):
    """
    Save portfolio to both TXT and CSV files
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save as TXT file
    txt_filename = f"portfolio_{timestamp}.txt"
    try:
        with open(txt_filename, 'w') as f:
            f.write("STOCK INVESTMENT TRACKER - PORTFOLIO REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write(f"{'Symbol':<8} {'Quantity':<10} {'Price':<10} {'Value':<12}\n")
            f.write("-" * 50 + "\n")
            
            for stock in portfolio:
                f.write(f"{stock['symbol']:<8} {stock['quantity']:<10.2f} ${stock['price']:<9.2f} ${stock['value']:<11.2f}\n")
            
            f.write("-" * 50 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total_investment:.2f}\n")
        
        print(f"✅ Portfolio saved as TXT: {txt_filename}")
    except Exception as e:
        print(f"❌ Error saving TXT file: {e}")
    
    # Save as CSV file
    csv_filename = f"portfolio_{timestamp}.csv"
    try:
        with open(csv_filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Symbol', 'Quantity', 'Price', 'Value', 'Timestamp'])
            
            for stock in portfolio:
                writer.writerow([
                    stock['symbol'],
                    stock['quantity'],
                    stock['price'],
                    stock['value'],
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
            
            # Add total row
            writer.writerow(['TOTAL', '', '', total_investment, ''])
        
        print(f"✅ Portfolio saved as CSV: {csv_filename}")
    except Exception as e:
        print(f"❌ Error saving CSV file: {e}")

def load_sample_portfolio():
    """
    Create a sample portfolio for demonstration
    """
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 135.20,
        "MSFT": 340.80,
        "NVDA": 485.60
    }
    
    sample_portfolio = [
        {'symbol': 'AAPL', 'quantity': 10, 'price': 180.50, 'value': 1805.00},
        {'symbol': 'TSLA', 'quantity': 5, 'price': 250.75, 'value': 1253.75},
        {'symbol': 'GOOGL', 'quantity': 8, 'price': 135.20, 'value': 1081.60}
    ]
    
    total = sum(stock['value'] for stock in sample_portfolio)
    
    print("📊 SAMPLE PORTFOLIO LOADED")
    display_portfolio_summary(sample_portfolio, total)
    
    choice = input("\nSave this sample portfolio? (y/n): ").lower().strip()
    if choice == 'y':
        save_portfolio(sample_portfolio, total)

def main():
    """
    Main function with menu options
    """
    print("🏦" + "=" * 48 + "🏦")
    print("       STOCK INVESTMENT TRACKER - TASK 2")
    print("🏦" + "=" * 48 + "🏦")
    
    while True:
        print(f"\nMain Menu:")
        print("1. Start Stock Tracker")
        print("2. Load Sample Portfolio")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            stock_tracker()
        elif choice == '2':
            load_sample_portfolio()
        elif choice == '3':
            print("Goodbye! Happy investing! 💰")
            break
        else:
            print("❌ Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()
