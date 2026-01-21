# Ask for initial investment
# Ask for interest rate as percentage
# Ask for number of years
# calculate value of each year, with compound interest
# Display year by year growth
# Display total profit at the end


initial_investment = float(input("Enter amount: "))
interest_rate = float(input("Enter rate (%): "))
no_of_years = int(input("Enter no of years: "))
current_amnt = initial_investment

print("\n" + "=" * 50)
print("INVESTMENT GROWTH PROJECTION")
print("=" * 50)
print("")
print(f"Initial Investement {initial_investment:,.2f}")
print(f"Interest rate {interest_rate}%")
print(f"Investment period {no_of_years} years")
print("")

for year in range(1, no_of_years + 1):
    interest_earned = current_amnt * (interest_rate/100)

    current_amnt = current_amnt * (1 + interest_rate/100)

    print(
        f"year{no_of_years}: ${current_amnt:,.2f} | Interest ${interest_earned:,.2f}")

total_profit = current_amnt-initial_investment

print("")
print("=" * 50)
print(f"Final amount {current_amnt:,.2f}")
print(f"Total Profit {total_profit:,.2f}")
print(f"Return on Investment {(total_profit/initial_investment)*100:.2f}%")
print("=" * 50)
