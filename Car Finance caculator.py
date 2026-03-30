# Ibrahim Mansour
# AutoLoan Pro - Car Financing Calculator with Loan Approval

def get_float(prompt):
    """Gets a valid float from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int(prompt):
    """Gets a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculate_monthly_payment(loan_amount, annual_rate, years):
    """Calculates monthly payment using loan formula."""
    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        return loan_amount / months

    payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / \
              ((1 + monthly_rate) ** months - 1)
    return payment

def check_approval(credit_score, monthly_income, monthly_payment):
    """Determines loan approval or denial."""
    if credit_score < 600:
        return False, "Denied: Credit score too low."

    if monthly_payment > monthly_income * 0.4:
        return False, "Denied: Payment exceeds 40% of monthly income."

    return True, "Approved!"

def display_results(loan_amount, monthly_payment, years, status, reason):
    """Displays final loan results."""
    total_paid = monthly_payment * years * 12
    interest_paid = total_paid - loan_amount

    print("\n----- Loan Summary -----")
    print(f"Loan Amount: ${loan_amount:.2f}")
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Paid: ${total_paid:.2f}")
    print(f"Total Interest: ${interest_paid:.2f}")
    print(f"Loan Status: {status}")
    print(f"Decision: {reason}")
    print("------------------------\n")

def main_menu():
    print("=== AutoLoan Pro ===")
    print("1. Apply for car loan")
    print("2. Exit")

def run_program():
    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            car_price = get_float("Enter car price: $")
            down_payment = get_float("Enter down payment: $")
            trade_in = get_float("Enter trade-in value: $")
            interest_rate = get_float("Enter annual interest rate (%): ")
            loan_years = get_int("Enter loan term (years): ")
            credit_score = get_int("Enter credit score: ")
            monthly_income = get_float("Enter monthly income: $")

            loan_amount = car_price - down_payment - trade_in

            if loan_amount <= 0:
                print("Loan amount must be greater than zero.")
                continue

            monthly_payment = calculate_monthly_payment(
                loan_amount, interest_rate, loan_years
            )

            approved, reason = check_approval(
                credit_score, monthly_income, monthly_payment
            )

            if approved:
                status = "APPROVED"
            else:
                status = "DENIED"

            display_results(
                loan_amount,
                monthly_payment,
                loan_years,
                status,
                reason
            )

        elif choice == "2":
            print("Thank you for using AutoLoan Pro!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
run_program()