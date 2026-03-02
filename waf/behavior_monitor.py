import time
from config import RATE_LIMIT_THRESHOLD, RATE_LIMIT_WINDOW

ip_tracker = {}

def check_rate_limit(ip):

    current_time = time.time()

    if ip not in ip_tracker:
        ip_tracker[ip] = []

    ip_tracker[ip].append(current_time)

    ip_tracker[ip] = [
        t for t in ip_tracker[ip]
        if current_time - t < RATE_LIMIT_WINDOW
    ]

    if len(ip_tracker[ip]) > RATE_LIMIT_THRESHOLD:
        return True

    return False