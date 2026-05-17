print("The ATM \"Multiples Only\" Cashier".center(50, " "))
while True:
    #input section
    c = input("Enter the Amount of Money (or type 'finish' to stop): ")

    #use of 'Finish' to stop the Do while Loop or loop
    if c in ['finish', 'Finish', 'FINISH']:
        print("The Process is now stopped. Goodbye!")
        break

    # for managing space in the input section
    if not c:
        print("Don't use any space in this Input section")
        continue
   #for managing the decimal number in the input section
    if "." in c:
        print("❌ Error: Decimal number is not allowed, please enter a multiple of 100.")
        continue  # This restarts the loop immediately, asking for input again

    try:
        # 2. Since we filtered out decimals above, we can safely convert to int
        d = int(c)

        if d <= 0:
            print("❌ Error: Please enter an amount greater than zero.")

        elif d % 100 == 0:
            print(f"✅ Success! Processing ${d}. Please collect your cash.")

        else:
            print("❌ Error: Invalid amount. Please enter a multiple of 100")

    except ValueError: #use for managing the iny kind of string input like hunderd instead of 100
        print("⚠️ That's not a valid number. Please use digits or type 'finish'.")
