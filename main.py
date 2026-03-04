from graph import app

result = app.invoke({
    "proposal": "Allocate $1M from the DAO treasury to lobby US regulators against the proposed DeFi broker reporting rules that would require on-chain protocols to collect KYC data from users",
    "advocate_argument": "",
    "critic_argument": "",
    "verdict": "",
    "confidence": 0,
    "round": 0
})

print("=== DEBATE RESULT ===")
print(f"Rounds: {result['round']}")
print(f"Verdict: {result['verdict']}")
print(f"Confidence: {result['confidence']}/10")