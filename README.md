# 🏦 Python ATM "Multiples Only" Cashier Interface

A highly secure, crash-resistant console application that simulates an ATM cash-dispensing mechanism with multi-layered input sanitization.

## 📝 Project Overview
In financial software, handling numerical input safely is critical. This project demonstrates advanced defensive programming in Python, ensuring that the system strictly processes valid transaction amounts (multiples of 100) while proactively catching formatting anomalies, text injections, and precision-loss traps.

## ⚙️ Core Logic & Advanced Edge-Case Handling
* **Multi-Layered Input Cleansing:** Utilizes the conditional checking (`if not c:`) system to immediately trap and flag accidental blank inputs or whitespace entries.
* **String-Level Decimal Isolation:** Rather than relying on float conversions—which introduce floating-point precision risks with extreme numbers—the script isolates decimals at the string level (`if "." in c:`) to protect financial logic integrity.
* **Infinite-Precision Integer Tracking:** By passing clean strings directly to `int()`, the script leverages Python's native support for arbitrarily large integers, maintaining mathematical accuracy for massive values.
* **Targeted Exception Handling:** Implements precise `except ValueError` blocks to elegantly catch and handle alphabetical inputs (e.g., typing "one hundred" instead of "100") without crashing the runtime.

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone this repository to your local system.
3. Run the script using your terminal: `python atm_cashier.py`
4. Test the system with boundary inputs (e.g., `100.1`, spaces, or massive integers) to see the defensive logic in action. Type `finish` to exit.
