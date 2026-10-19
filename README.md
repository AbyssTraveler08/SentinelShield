<div align="center">

# 🕷️ SentinelShield

**A Flask-based web-protection prototype with rule-based request inspection, rate limiting, blocking decisions, event logging, and a dashboard.**

<img src="https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/Focus-Web%20Security-0A66C2?style=for-the-badge" alt="Web security" />
<img src="https://img.shields.io/badge/Stage-Educational%20Prototype-475569?style=for-the-badge" alt="Educational prototype" />

</div>

---

## 🔎 Overview

SentinelShield is an educational web-protection prototype that inspects incoming Flask requests, applies regular-expression rules, checks a basic per-IP request-rate threshold, and chooses to allow or block the request. It also provides a dashboard route for viewing generated security-event summaries.

The project demonstrates separation of request inspection, rule matching, behavioral checks, decision logic, and logging. It is **not a production-ready Web Application Firewall (WAF)** and should be used only in a local or isolated lab.

## ✨ Detection capabilities

- Rule-based patterns for selected SQL injection indicators.
- Basic cross-site scripting (XSS) string detection.
- Local file inclusion / directory-traversal indicators.
- Basic command-injection string patterns.
- In-memory rate tracking by client IP.
- Central decision engine returning ALLOW or BLOCK.
- Security event logging for blocked requests.
- Flask test interface and dashboard route.

## 🧭 Request flow

~~~text
Incoming Flask request
          |
          v
Inspect URL, headers, and body
          |
          +------> Match detection rules
          |
          +------> Check request-rate threshold
                         |
                         v
                  Decision engine
                   /           \
                ALLOW          BLOCK
                  |              |
                  v              v
              Web page      Log event + 403
                                 |
                                 v
                           Dashboard data
~~~

## 🧰 Requirements

- Python 3.
- Flask.
- A local test environment.

The repository does not currently include a requirements.txt file, so install Flask in a virtual environment.

## ⚙️ Installation and setup

~~~bash
git clone https://github.com/AbyssTraveler08/SentinelShield.git
cd SentinelShield

python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask
mkdir -p logs
~~~

## 🚀 Run locally

~~~bash
python3 app.py
~~~

Open **http://127.0.0.1:5000/**. The dashboard route is **http://127.0.0.1:5000/dashboard**. Keep the process local and stop it with Ctrl+C when finished.

Create the logs directory before testing block events, because the configured log file lives under **logs/security.log**.

## 🗂️ Code structure

| Path | Responsibility |
|---|---|
| **app.py** | Flask routes and request orchestration |
| **config.py** | Rate-limit thresholds and log path |
| **waf/request_inspector.py** | Combines request data for inspection |
| **waf/rule_engine.py** | Regex-based attack-indicator patterns |
| **waf/behavior_monitor.py** | In-memory request-rate tracking |
| **waf/decision_engine.py** | ALLOW/BLOCK decision |
| **logger/security_logger.py** | Security event logging |
| **dashboard/dashboard_engine.py** | Dashboard summary data |
| **templates/** | Main and dashboard HTML templates |

## 🧪 Safe testing

Test only against the local instance using benign requests and controlled test strings. Review the returned status code and generated log entries. Do not use real attack payloads against third-party applications or production services.

## ⚠️ Security limitations

- The rules are simple regular expressions and can produce false positives and false negatives.
- Rate tracking is process-local and resets when the app restarts; it is not a distributed rate limiter.
- The current configuration uses Flask's development server with debug mode enabled. Do not expose it to the internet.
- Request parsing and sample rules are not sufficient for comprehensive WAF protection.
- Production deployment would require hardened configuration, structured logging, tests, rule tuning, and a defense-in-depth review.

## 🗺️ Roadmap

- Add a requirements file and automated tests.
- Add structured event fields and improved dashboard filtering.
- Make rules configurable and add tests for false positives.
- Implement bounded and concurrency-safe rate tracking.
- Add production-safe configuration before any deployment.

## 👤 Author

**Amar Kant Yadav** · [GitHub profile](https://github.com/AbyssTraveler08)

## 📄 License

See the repository's LICENSE file.

---

<div align="center">Built to explore request inspection and defensive web-security concepts.</div>
