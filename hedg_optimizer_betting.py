# Входни данни
print("🎰 СИСТЕМА ЗА ХЕДЖИРАНЕ - ТОЧЕН ПОДХОД")
print("=" * 60)

coef = [float(x) for x in input("Въведете коефициенти (1 X 2): ").split()]
bets = [float(x) for x in input("Въведете залози (1 X 2): ").split()]

total_income = sum(bets)

print(f"\n📊 ВХОДНИ ДАННИ:")
print(f"1: {bets[0]}лв @ {coef[0]} → Плащане: {bets[0] * coef[0]:.0f}лв")
print(f"X: {bets[1]}лв @ {coef[1]} → Плащане: {bets[1] * coef[1]:.0f}лв")
print(f"2: {bets[2]}лв @ {coef[2]} → Плащане: {bets[2] * coef[2]:.0f}лв")
print(f"Общ приход: {total_income}лв")
print("=" * 60)

# Хеджиращи коефициенти (2% дисконт)
hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]

payouts = [bets[i] * coef[i] for i in range(3)]

# СТЪПКА 1: Намиране на касата (най-висок коефициент)
highest_coef_index = coef.index(max(coef))
cash = payouts[highest_coef_index]
excess = total_income - cash

print(f"\n💰 ОСНОВНА КАСА:")
print(f"   Каса ({['1', 'X', '2'][highest_coef_index]}): {cash:.0f}лв")
print(f"   Излишък: {excess:.0f}лв")

# СТЪПКА 2: Изчисляване на дефицитите
deficits = []
for i in range(3):
    if i != highest_coef_index:
        deficit = payouts[i] - cash
        deficits.append((i, deficit))

print(f"\n📉 ДЕФИЦИТИ:")
for i, deficit in deficits:
    print(f"   {['1', 'X', '2'][i]}: {deficit:.0f}лв")

# СТЪПКА 3: ПОКРИВАНЕ НА ДЕФИЦИТИТЕ С ТОЧНИ СУМИ
hedge_amounts = [0, 0, 0]
remaining_excess = excess

print(f"\n🛡️ ПОКРИВАНЕ НА ДЕФИЦИТИТЕ:")
for i, deficit in deficits:
    # ТОЧНА формула: дефицит / коефициент
    hedge_amount = deficit / hedge_coefs[i]

    if hedge_amount <= remaining_excess:
        hedge_amounts[i] = hedge_amount
        remaining_excess -= hedge_amount
        print(f"   {['1', 'X', '2'][i]}: {deficit:.0f}лв / {hedge_coefs[i]:.2f} = {hedge_amount:.0f}лв")

# СТЪПКА 4: Разпределяне на оставащия излишък
print(f"\n🔄 РАЗПРЕДЕЛЯНЕ НА ОСТАТЪКА:")
print(f"   Оставащ излишък: {remaining_excess:.0f}лв")

if remaining_excess > 0:
    # Сума на коефициентите за двата други изхода
    other_outcomes = [i for i in range(3) if i != highest_coef_index]
    sum_other_coef = hedge_coefs[other_outcomes[0]] + hedge_coefs[other_outcomes[1]]

    base_amount = remaining_excess / sum_other_coef

    print(f"   Базова стойност: {remaining_excess:.0f} / {sum_other_coef:.2f} = {base_amount:.0f}лв")

    for i in other_outcomes:
        other_coef = hedge_coefs[[x for x in other_outcomes if x != i][0]]
        additional_hedge = other_coef * base_amount
        hedge_amounts[i] += additional_hedge
        print(f"   {['1', 'X', '2'][i]}: {other_coef:.2f} × {base_amount:.0f} = {additional_hedge:.0f}лв")

# СТЪПКА 5: ФИНАЛНИ РЕЗУЛТАТИ
print(f"\n🎲 ФИНАЛНА СИМУЛАЦИЯ:")
print("=" * 60)

total_hedge = sum(hedge_amounts)
final_cash = total_income - total_hedge

for i in range(3):
    outcome = ["1", "X", "2"][i]
    payout = payouts[i]

    hedge_income = hedge_amounts[i] * hedge_coefs[i]
    result = final_cash + hedge_income - payout

    margin = (result / total_income) * 100

    print(f"🔮 {outcome}:")
    print(f"   Каса: {final_cash:.0f}лв")
    if hedge_income > 0:
        print(f"   Хедж: +{hedge_income:.0f}лв")
    print(f"   Плащане: -{payout:.0f}лв")
    print(f"   РЕЗУЛТАТ: {result:.0f}лв ({margin:+.1f}%)")
    print("-" * 40)

print(f"\n📈 ОБЩА СТАТИСТИКА:")
print(f"   Приход: {total_income:.0f}лв")
print(f"   Хедж: {total_hedge:.0f}лв")
print(f"   Каса: {final_cash:.0f}лв")
print("=" * 60)