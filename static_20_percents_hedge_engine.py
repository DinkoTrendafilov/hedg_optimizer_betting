coef = [float(x) for x in input("Enter odds (1 X 2): ").split()]
bets = [float(x) for x in input("Enter bets (1 X 2): ").split()]

total_income = sum(bets)

print(f"\nINPUT DATA:")
print(f"1: {bets[0]:_} at {coef[0]:_} → Payout: {bets[0] * coef[0]:_.0f}")
print(f"X: {bets[1]:_} at {coef[1]:_} → Payout: {bets[1] * coef[1]:_.0f}")
print(f"2: {bets[2]:_} at {coef[2]:_} → Payout: {bets[2] * coef[2]:_.0f}")
print(f"Total income: {total_income:_}")
print("=" * 112)

hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]

payouts = [bets[i] * coef[i] for i in range(3)]

cash = total_income * 0.80
hedge_budget = total_income * 0.20

print(f"STRATEGY: STATIC 80% CASH")
print(f"\nBASE CASH:")
print(f"   Cash: {cash:_.0f} (80% от дохода)")
print(f"   Hedge budget: {hedge_budget:_.0f} (20% от дохода)")

deficits = []
for i in range(3):
    deficit = payouts[i] - cash
    deficits.append((i, deficit))

print(f"\nDEFICITS:")
for i, deficit in deficits:
    print(f"   {['1', 'X', '2'][i]}: {deficit:_.0f}")

hedge_amounts = [0, 0, 0]
remaining_hedge = hedge_budget

print(f"\nCOVERING DEFICITS:")
for i, deficit in deficits:
    if deficit > 0 and remaining_hedge > 0:
        hedge_amount = deficit / hedge_coefs[i]

        actual_hedge = min(hedge_amount, remaining_hedge)
        hedge_amounts[i] = actual_hedge
        remaining_hedge -= actual_hedge
        print(f"   {['1', 'X', '2'][i]}: {deficit:_.0f} / {hedge_coefs[i]:_.2f} = {actual_hedge:_.0f}")

print(f"\nDISTRIBUTING REMAINDER (INVERSELY PROPORTIONAL):")
print(f"   Remaining hedge budget: {remaining_hedge:_.0f}")

if remaining_hedge > 0:

    reverse_coefs = [coef[2], coef[1], coef[0]]

    total_reverse = sum(reverse_coefs)

    print(f"   Inverse odds: {reverse_coefs[0]}, {reverse_coefs[1]}, {reverse_coefs[2]}")
    print(f"   Sum of inverse: {total_reverse:.1f}")

    for i in range(3):
        additional_hedge = (reverse_coefs[i] / total_reverse) * remaining_hedge
        hedge_amounts[i] += additional_hedge
        print(
            f"   {['1', 'X', '2'][i]}: {reverse_coefs[i]:.1f}/{total_reverse:.1f} × {remaining_hedge:_.0f} = {additional_hedge:_.0f}")

total_hedge = sum(hedge_amounts)
if abs(total_hedge - hedge_budget) > 1:
    print(f"\nCORRECTION: Hedge = {total_hedge:_.0f} → {hedge_budget:_.0f}")
    correction_factor = hedge_budget / total_hedge
    for i in range(3):
        hedge_amounts[i] *= correction_factor
    total_hedge = sum(hedge_amounts)

print(f"\nFINAL SIMULATION:")
print("=" * 112)

final_cash = cash

print(f"REAL EXPENSES:")
print(f"   Hedge budget: {hedge_budget:_.0f}")
print(f"   Actual hedge: {total_hedge:_.0f}")
print(f"   Cash: {final_cash:_.0f}")
print(f"   Total expense: {total_hedge + final_cash:_.0f}")

for i in range(3):
    outcome = ["1", "X", "2"][i]
    payout = payouts[i]

    hedge_income = hedge_amounts[i] * hedge_coefs[i]
    result = final_cash + hedge_income - payout

    margin = (result / total_income) * 100

    print(f"\nSCENARIO {outcome}:")
    print(f"   Cash: {final_cash:_.0f}")
    print(f"   Hedge: +{hedge_income:_.0f}")
    print(f"   Payout: -{payout:_.0f}")
    print(f"   RESULT: {result:_.0f} ({margin:+.1f} %)")

print(f"\nOVERALL STATISTICS:")
print(f"   Income: {total_income:_.0f}")
print(f"   Hedge: {total_hedge:_.0f}")
print(f"   Cash: {final_cash:_.0f}")
print(f"   Total expense: {total_hedge + final_cash:_.0f}")
print("=" * 112)
