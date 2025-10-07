# 🎰 Quant Hedge Engine

**Author:** Dinko Trendafilov  
**Language:** Python 3  
**Version:** 1.0  
**Focus:** Dynamic hedge optimization and exposure balancing for 1X2 betting markets  

---

## 🧭 Project Motivation

In professional betting and trading environments, the ability to **precisely balance exposure** determines whether a sportsbook operates with stability or chaos.  
This project was built to **demonstrate quantitative hedge thinking** — how surplus capital can be reallocated across outcomes to maintain equilibrium and protect profit margins.  

It reflects the mindset of a **risk analyst or trading strategist**, using code to quantify control, precision, and foresight in decision-making.  

---

## 🧩 Overview

**Quant Hedge Engine** is a precision-based Python system that simulates how a sportsbook can hedge exposure across 1X2 markets using a step-by-step quantitative model.  

It redistributes excess funds dynamically to minimize risk and stabilize overall portfolio variance — a realistic and explainable model for internal sportsbook risk tools or academic research on hedge optimization.

---

## ⚙️ Example Run

```bash
🎰 HEDGING SYSTEM - PRECISE APPROACH
============================================================

Enter odds (1 X 2): 2.4 3.3 3.1
Enter stakes (1 X 2): 100 80 120
Output includes:

Input summary (bets, odds, and total exposure)

Main “cash” line (highest return position)

Deficit calculation for weaker outcomes

Exact hedge distribution using a 2% discount factor

Residual fund redistribution

Final profit/loss simulation with margin per outcome

🧮 Logic Breakdown
Step	Description
1	Input odds & stake distribution
2	Identify the primary cash position (highest payout)
3	Compute exposure deficits across other outcomes
4	Allocate hedge funds with a 2% discount precision factor
5	Redistribute remaining surplus proportionally
6	Simulate final P/L and margin across all possible outcomes

📊 Core Features
🔹 Dynamic hedge coefficient adjustment (2% precision discount)

🔹 Automated deficit detection & coverage

🔹 Residual surplus redistribution logic

🔹 Complete financial simulation per outcome

🔹 No dependencies — pure, transparent Python code

🧠 Why It Matters
In a betting company, hedging is not gambling — it’s engineering.
This project demonstrates how analytical models can:

Detect structural inefficiencies between odds and exposure

Redistribute liquidity to stabilize risk

Show measurable improvement in expected margin consistency

It represents a quant mindset — building logic before profit, precision before luck.

🚀 Future Enhancements
Integration with real-time odds APIs

Multi-market expansion (Asian Handicap / Over-Under)

Exposure curve visualization (Matplotlib / Plotly)

Full web dashboard (FastAPI + React) for internal trading desks

🧰 Tech Stack
Language: Python 3.x

Interface: Command Line (CLI)

Dependencies: None

Complexity: O(n) linear — optimized for transparency and speed

💼 Use Case
Designed for sportsbook analysts, risk managers, and trading teams exploring hedge optimization logic in real 1X2 environments.

Can also be adapted for:

Portfolio exposure balancing

Monte Carlo hedge simulations

Academic demonstration of quantitative betting models

📄 License
MIT License © 2025 — Dinko Trendafilov

“A trading desk without hedge logic is a casino.
A casino with hedge logic becomes a trading desk.”
— Dinko Trendafilov
