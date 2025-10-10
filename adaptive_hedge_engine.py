# Input data
print("HEDGING SYSTEM - ADAPTIVE APPROACH")
print("=" * 112)

coef = [float(x) for x in input("Enter odds (1 X 2): ").split()]
bets = [float(x) for x in input("Enter bets (1 X 2): ").split()]

total_income = sum(bets)

print(f"\nINPUT DATA:")
print(f"1: {bets[0]:_} at {coef[0]:_} → Payout: {bets[0] * coef[0]:_.0f}")
print(f"X: {bets[1]:_} at {coef[1]:_} → Payout: {bets[1] * coef[1]:_.0f}")
print(f"2: {bets[2]:_} at {coef[2]:_} → Payout: {bets[2] * coef[2]:_.0f}")
print(f"Total income: {total_income:_}")
print("=" * 112)

# Hedging odds (2% discount)
hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]

payouts = [bets[i] * coef[i] for i in range(3)]

# STEP 1: STRATEGY SELECTION
max_coef = max(coef)
min_payout = min(payouts)
min_payout_index = payouts.index(min_payout)

if max_coef >= 4:
    # STRATEGY 1: Based on highest odds
    highest_coef_index = coef.index(max_coef)
    cash = payouts[highest_coef_index]
    strategy_name = "HIGH ODDS"
    base_index = highest_coef_index
    print(f"STRATEGY: HIGH ODDS ({max_coef} ≥ 4)")
else:
    # STRATEGY 2: Based on no clear favorite
    cash = min_payout
    strategy_name = "NO CLEAR FAVORITE"
    base_index = min_payout_index
    print(f"STRATEGY: NO CLEAR FAVORITE ({max_coef} < 4)")

excess = total_income - cash

print(f"\nBASE CASH:")
print(f"   Strategy: {strategy_name}")
print(f"   Base ({['1', 'X', '2'][base_index]}): {cash:_.0f}")
print(f"   Excess: {excess:_.0f}")

# STEP 2: Calculate deficits
deficits = []
for i in range(3):
    if i != base_index:
        deficit = payouts[i] - cash
        deficits.append((i, deficit))

print(f"\nDEFICITS:")
for i, deficit in deficits:
    print(f"   {['1', 'X', '2'][i]}: {deficit:_.0f}")

# STEP 3: COVER DEFICITS WITH EXACT AMOUNTS
hedge_amounts = [0, 0, 0]
remaining_excess = excess

print(f"\nCOVERING DEFICITS:")
for i, deficit in deficits:
    # EXACT formula: deficit / odds
    hedge_amount = deficit / hedge_coefs[i]

    if hedge_amount <= remaining_excess:
        hedge_amounts[i] = hedge_amount
        remaining_excess -= hedge_amount
        print(f"   {['1', 'X', '2'][i]}: {deficit:_.0f} / {hedge_coefs[i]:_.2f} = {hedge_amount:_.0f}")

# STEP 4: Distribute remaining excess
print(f"\nDISTRIBUTING REMAINDER:")
print(f"   Remaining excess: {remaining_excess:_.0f}")

if remaining_excess > 0:
    # Sum of odds for the two other outcomes
    other_outcomes = [i for i in range(3) if i != base_index]
    sum_other_coef = hedge_coefs[other_outcomes[0]] + hedge_coefs[other_outcomes[1]]

    base_amount = remaining_excess / sum_other_coef

    print(f"   Base value: {remaining_excess:_.0f} / {sum_other_coef:_.2f} = {base_amount:_.0f}")

    for i in other_outcomes:
        other_coef = hedge_coefs[[x for x in other_outcomes if x != i][0]]
        additional_hedge = other_coef * base_amount
        hedge_amounts[i] += additional_hedge
        print(f"   {['1', 'X', '2'][i]}: {other_coef:_.2f} × {base_amount:_.0f} = {additional_hedge:_.0f}")

# STEP 5: FINAL RESULTS
print(f"\nFINAL SIMULATION:")
print("=" * 112)

total_hedge = sum(hedge_amounts)
final_cash = total_income - total_hedge

for i in range(3):
    outcome = ["1", "X", "2"][i]
    payout = payouts[i]

    hedge_income = hedge_amounts[i] * hedge_coefs[i]
    result = final_cash + hedge_income - payout

    margin = (result / total_income) * 100

    print(f"SCENARIO {outcome}:")
    print(f"   Cash: {final_cash:_.0f}")
    if hedge_income > 0:
        print(f"   Hedge: +{hedge_income:_.0f}")
    print(f"   Payout: -{payout:_.0f}")
    print(f"   RESULT: {result:_.0f} ({margin:+.1f} %)")
    print("-" * 40)

print(f"\nOVERALL STATISTICS:")
print(f"   Income: {total_income:_.0f}")
print(f"   Hedge: {total_hedge:_.0f}")
print(f"   Cash: {final_cash:_.0f}")
print(f"   Strategy: {strategy_name}")
print("=" * 112)
