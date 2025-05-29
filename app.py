
import time
import random
from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)

# === CONFIG ===
AFFILIATE_LINK = "https://forgeniuswave.com/DSvsl/#aff=Ross803"
COURSES = [
    "AI Side Hustle Course",
    "No-Face TikTok Monetization",
    "ChatGPT Passive Income Workshop",
    "Affiliate Marketing Bootcamp",
    "Sell Digital Products in Your Sleep"
]
PRICES = [29, 49, 99, 149, 199]

# === LEAD FUNNEL ===
leads = []
sales = []

@app.route("/traffic", methods=["POST"])
def incoming_traffic():
    ip = request.remote_addr
    leads.append({"ip": ip, "timestamp": time.time()})
    if random.random() < 0.25:
        course = random.choice(COURSES)
        price = random.choice(PRICES)
        sales.append({"course": course, "price": price, "ip": ip, "timestamp": time.time()})
        return jsonify({"status": "converted", "course": course, "price": price})
    return jsonify({"status": "lead", "message": "Saved for remarketing."})

@app.route("/leads", methods=["GET"])
def show_leads():
    return jsonify(leads)

@app.route("/sales", methods=["GET"])
def show_sales():
    total = sum(s['price'] for s in sales)
    return jsonify({"total_sales": total, "sales": sales})

# === SIMULATED TRAFFIC ENGINE ===
def fake_traffic():
    while True:
        try:
            with app.test_client() as c:
                c.post("/traffic")
            time.sleep(random.uniform(1, 4))
        except:
            pass

Thread(target=fake_traffic, daemon=True).start()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
