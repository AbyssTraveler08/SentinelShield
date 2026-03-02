import re

class RuleEngine:

    def __init__(self):
        self.rules = {
            "SQL Injection": [
                r"(\bUNION\b|\bSELECT\b|\bOR\b\s+1=1)",
                r"(--|#)"
            ],
            "XSS": [
                r"<script.*?>.*?</script>",
                r"javascript:",
                r"onerror="
            ],
            "LFI / Directory Traversal": [
                r"\.\./",
                r"/etc/passwd"
            ],
            "Command Injection": [
                r";\s*\w+",
                r"&&",
                r"\|\|"
            ]
        }

    def detect(self, data):
        for attack_type, patterns in self.rules.items():
            for pattern in patterns:
                if re.search(pattern, data, re.IGNORECASE):
                    return attack_type
        return None