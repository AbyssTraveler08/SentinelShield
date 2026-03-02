from flask import Flask, request, render_template
from waf.request_inspector import inspect_request
from waf.behavior_monitor import check_rate_limit
from waf.decision_engine import make_decision
from logger.security_logger import log_event
from dashboard.dashboard_engine import generate_dashboard_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    ip = request.remote_addr

    rate_flag = check_rate_limit(ip)

    detection = inspect_request(request)

    decision = make_decision(detection, rate_flag)

    if decision["action"] == "BLOCK":
        log_event(ip, decision["reason"])
        return f"Blocked by SentinelShield: {decision['reason']}", 403

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    data = generate_dashboard_data()

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)