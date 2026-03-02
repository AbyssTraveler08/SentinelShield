from collections import Counter
from config import LOG_FILE

def generate_dashboard_data():

    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
    except:
        return {}

    attack_types = []
    ips = []

    for line in lines:
        parts = line.split("|")
        if len(parts) >= 3:
            ips.append(parts[1].strip())
            attack_types.append(parts[2].strip())

    return {
        "total_attacks": len(lines),
        "attack_distribution": dict(Counter(attack_types)),
        "ip_distribution": dict(Counter(ips))
    }