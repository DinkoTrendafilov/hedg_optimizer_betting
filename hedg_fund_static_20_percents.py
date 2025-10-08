# Входни данни
print("🎰 СИСТЕМА ЗА ХЕДЖИРАНЕ - СТАТИЧНА КАСА 80%")
print("=" * 112)

coef = [float(x) for x in input("Въведете коефициенти (1 X 2): ").split()]
bets = [float(x) for x in input("Въведете залози (1 X 2): ").split()]

total_income = sum(bets)

print(f"\n📊 ВХОДНИ ДАННИ:")
print(f"1: {bets[0]:_} лв @ {coef[0]:_} → Плащане: {bets[0] * coef[0]:_.0f} лв")
print(f"X: {bets[1]:_} лв @ {coef[1]:_} → Плащане: {bets[1] * coef[1]:_.0f} лв")
print(f"2: {bets[2]:_} лв @ {coef[2]:_} → Плащане: {bets[2] * coef[2]:_.0f} лв")
print(f"Общ приход: {total_income:_} лв")
print("=" * 112)

# Хеджиращи коефициенти (2% дисконт)
hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]

payouts = [bets[i] * coef[i] for i in range(3)]

# СТЪПКА 1: СТАТИЧНА КАСА 80%
cash = total_income * 0.80
hedge_budget = total_income * 0.20

print(f"🎯 СТРАТЕГИЯ: СТАТИЧНА КАСА 80%")
print(f"\n💰 ОСНОВНА КАСА:")
print(f"   Каса: {cash:_.0f} лв (80% от прихода)")
print(f"   Хедж бюджет: {hedge_budget:_.0f} лв (20% от прихода)")

# СТЪПКА 2: Изчисляване на дефицитите
deficits = []
for i in range(3):
    deficit = payouts[i] - cash
    deficits.append((i, deficit))

print(f"\n📉 ДЕФИЦИТИ:")
for i, deficit in deficits:
    print(f"   {['1', 'X', '2'][i]}: {deficit:_.0f} лв")

# СТЪПКА 3: ПОКРИВАНЕ НА ДЕФИЦИТИТЕ
hedge_amounts = [0, 0, 0]
remaining_hedge = hedge_budget

print(f"\n🛡️ ПОКРИВАНЕ НА ДЕФИЦИТИТЕ:")
for i, deficit in deficits:
    if deficit > 0 and remaining_hedge > 0:
        hedge_amount = deficit / hedge_coefs[i]
        # Вземаме колкото можем от оставащия бюджет
        actual_hedge = min(hedge_amount, remaining_hedge)
        hedge_amounts[i] = actual_hedge
        remaining_hedge -= actual_hedge
        print(f"   {['1', 'X', '2'][i]}: {deficit:_.0f} лв / {hedge_coefs[i]:_.2f} = {actual_hedge:_.0f} лв")

# СТЪПКА 4: РАЗПРЕДЕЛЯНЕ НА ОСТАТЪКА
print(f"\n🔄 РАЗПРЕДЕЛЯНЕ НА ОСТАТЪКА:")
print(f"   Оставащ хедж бюджет: {remaining_hedge:_.0f} лв")

if remaining_hedge > 0:
    product_all = coef[0] * coef[1] * coef[2]
    base_amount = remaining_hedge / product_all

    print(f"   Произведение на коефициентите: {product_all:.1f}")
    print(f"   Базова стойност: {remaining_hedge:_.0f} / {product_all:.1f} = {base_amount:_.0f} лв")

    for i in range(3):
        other_coef_product = coef[(i + 1) % 3] * coef[(i + 2) % 3]
        additional_hedge = base_amount * other_coef_product
        hedge_amounts[i] += additional_hedge
        print(f"   {['1', 'X', '2'][i]}: {base_amount:_.0f} × {other_coef_product:.1f} = {additional_hedge:_.0f} лв")

# ГАРАНТИРАМЕ, че хеджа е ТОЧНО 20%
total_hedge = sum(hedge_amounts)
if abs(total_hedge - hedge_budget) > 1:
    print(f"\n⚖️  КОРИГИРАНЕ: Хедж = {total_hedge:_.0f} лв → {hedge_budget:_.0f} лв")
    correction_factor = hedge_budget / total_hedge
    for i in range(3):
        hedge_amounts[i] *= correction_factor
    total_hedge = sum(hedge_amounts)

# СТЪПКА 5: ФИНАЛНИ РЕЗУЛТАТИ
print(f"\n🎲 ФИНАЛНА СИМУЛАЦИЯ:")
print("=" * 112)

final_cash = cash  # Касата ВИНАГИ е 80% от прихода

print(f"📊 РЕАЛНИ ИЗРАЗХОДВАНИЯ:")
print(f"   Хедж бюджет: {hedge_budget:_.0f} лв")
print(f"   Реален хедж: {total_hedge:_.0f} лв")
print(f"   Каса: {final_cash:_.0f} лв")
print(f"   Общ разход: {total_hedge + final_cash:_.0f} лв")

for i in range(3):
    outcome = ["1", "X", "2"][i]
    payout = payouts[i]

    hedge_income = hedge_amounts[i] * hedge_coefs[i]
    result = final_cash + hedge_income - payout

    margin = (result / total_income) * 100

    print(f"\n🔮 {outcome}:")
    print(f"   Каса: {final_cash:_.0f} лв")
    print(f"   Хедж: +{hedge_income:_.0f} лв")
    print(f"   Плащане: -{payout:_.0f} лв")
    print(f"   РЕЗУЛТАТ: {result:_.0f} лв ({margin:+.1f} %)")

print(f"\n📈 ОБЩА СТАТИСТИКА:")
print(f"   Приход: {total_income:_.0f} лв")
print(f"   Хедж: {total_hedge:_.0f} лв")
print(f"   Каса: {final_cash:_.0f} лв")
print(f"   Общ разход: {total_hedge + final_cash:_.0f} лв")
print("=" * 112)
