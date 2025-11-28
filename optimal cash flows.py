coefficients = [float(x) for x in input().split()]
total_income = float(input())

implicit_coefficients = sum([(1 / x) for x in coefficients])

profit_percentage = (1 - (1 / implicit_coefficients)) * 100

needed_bet_money = total_income / implicit_coefficients

print(f"Sum of reciprocal coefficients: {implicit_coefficients:.4f}")
print(f"Company profit margin: {profit_percentage:.2f}%")
print(f"Total bet amount needed: {needed_bet_money:.2f}")
print()

d = ["1", "X", "2"]
for i, el in enumerate(coefficients):
    result = needed_bet_money / el
    bet_type = d[i] if i < len(d) else str(i + 1)
    print(f"{bet_type}: Bet {result:.2f} at coefficient {el}")
