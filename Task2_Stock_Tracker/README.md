# Task 2: Stock Investment Tracker

## Goal
Build a simple stock tracker that calculates total investment based on manually defined stock prices.

## Requirements Met
- ✅ User inputs stock names and quantity
- ✅ Uses hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250})
- ✅ Displays total investment value
- ✅ Optionally saves the result in both .txt and .csv files

## Files
- `stock_tracker.py` - Main application implementation
- `README.md` - Project documentation

## How to Run
1. Open terminal/command prompt
2. Navigate to the Task2_Stock_Tracker folder
3. Run: `python stock_tracker.py`

## Features
### Stock Database
10 predefined stocks with hardcoded prices:
- **AAPL** - $180.50 (Apple Inc.)
- **TSLA** - $250.75 (Tesla Inc.)
- **GOOGL** - $135.20 (Alphabet Inc.)
- **MSFT** - $340.80 (Microsoft Corporation)
- **AMZN** - $145.30 (Amazon.com Inc.)
- **NVDA** - $485.60 (NVIDIA Corporation)
- **META** - $325.15 (Meta Platforms Inc.)
- **NFLX** - $445.90 (Netflix Inc.)
- **PYPL** - $58.25 (PayPal Holdings Inc.)
- **AMD** - $115.40 (Advanced Micro Devices)

### Core Functionality
1. **Add Stocks to Portfolio**
   - Enter stock symbol and quantity
   - Automatic calculation of investment value
   - Input validation and error handling

2. **Portfolio Management**
   - View detailed portfolio summary
   - Track total investment value
   - Add multiple stocks to build a diversified portfolio

3. **File Export Options**
   - Save portfolio as TXT file (formatted report)
   - Save portfolio as CSV file (spreadsheet-ready)
   - Timestamped filenames for organization

4. **Sample Portfolio**
   - Pre-loaded example portfolio for demonstration
   - Quick way to test the application features

## Key Concepts Demonstrated
- **Dictionaries** - Stock price storage and lookup
- **Lists** - Portfolio management
- **File I/O** - TXT and CSV file operations
- **Input validation** - Error handling for user inputs
- **String formatting** - Clean console output
- **DateTime** - Timestamp generation
- **CSV module** - Structured data export
- **Exception handling** - Robust error management

## Example Usage

### Adding Stocks
```
Enter stock symbol (e.g., AAPL): AAPL
Enter quantity for AAPL: 10
✅ Added 10.0 shares of AAPL at $180.50 each
Investment value: $1805.00
```

### Portfolio Summary
```
📋 PORTFOLIO SUMMARY
============================================================
Symbol   Quantity   Price      Value       
------------------------------------------------------------
AAPL     10.00      $180.50    $1805.00   
TSLA     5.00       $250.75    $1253.75   
GOOGL    8.00       $135.20    $1081.60   
------------------------------------------------------------
TOTAL INVESTMENT:                      $4140.35
============================================================
```

### File Output
- **TXT Format**: Human-readable formatted report
- **CSV Format**: Spreadsheet-compatible with headers
- **Filenames**: `portfolio_YYYYMMDD_HHMMSS.txt/csv`

## Input Validation
- Stock symbol must exist in database
- Quantity must be a positive number
- Handles invalid inputs gracefully
- Provides helpful error messages

## Menu System
1. **Main Menu**
   - Start Stock Tracker
   - Load Sample Portfolio
   - Exit

2. **Stock Tracker Menu**
   - Add stock to portfolio
   - View portfolio summary
   - Save portfolio to file
   - Exit

## Learning Outcomes
This task demonstrates:
- Dictionary operations and lookups
- User input handling and validation
- File operations (both TXT and CSV)
- Menu-driven program structure
- Data organization and presentation
- Error handling and user experience
- Mathematical calculations
- String formatting and console output
