def make_decision(detection, rate_flag):

    if rate_flag:
        return {
            "action": "BLOCK",
            "reason": "Rate Limit Exceeded"
        }

    if detection:
        return {
            "action": "BLOCK",
            "reason": detection
        }

    return {
        "action": "ALLOW",
        "reason": "Normal"
    }
