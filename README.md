# 🎰 Quant Hedge Engine for Betting Companies

**Version:** 1.0  
**Author:** Dinko Trendafilov  
**Language:** Python 3  
**Focus:** Hedge optimization and risk balancing for betting portfolios  

---

## 🧩 Overview

This project simulates a **hedging system for 1X2 betting markets**, designed for internal use in a sportsbook or trading team.  
The algorithm demonstrates *how excess cash flow can be redistributed to minimize exposure across outcomes* using a dynamic hedge model.

It applies a **precision-based approach** to:
- Identify the strongest market (highest coefficient)
- Calculate the surplus (excess funds)
- Redistribute it to cover exposure on other outcomes
- Adjust for small discrepancies (2% hedge discount)
- Simulate final profit margins across outcomes

---

## ⚙️ Example Workflow

```bash
🎰 СИСТЕМА ЗА ХЕДЖИРАНЕ - ТОЧЕН ПОДХОД
============================================================

Въведете коефициенти (1 X 2): 2.4 3.3 3.1
Въведете залози (1 X 2): 100 80 120
The program outputs:

Initial bets and payouts

Main "cash" line (highest coefficient outcome)

Deficit calculations

Exact hedge amounts

Final simulated results with margin per outcome

📊 Key Features
✅ Dynamic hedge coefficient adjustment (2% discount factor)

✅ Automatic deficit balancing

✅ Residual redistribution logic for precision coverage

✅ Complete financial simulation per outcome

✅ Easy to modify for real odds feed or live trading desk

🧮 Core Logic
Step	Description
1	Input coefficients & bets
2	Identify main cash position
3	Compute exposure (deficits)
4	Allocate hedge funds with discount
5	Redistribute remaining balance
6	Simulate profit/loss across all outcomes
