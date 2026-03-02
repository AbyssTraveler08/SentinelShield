from waf.rule_engine import RuleEngine

rule_engine = RuleEngine()

def inspect_request(req):

    combined_data = ""

    combined_data += req.url

    for header in req.headers:
        combined_data += str(header)

    if req.data:
        combined_data += req.data.decode(errors="ignore")

    detection = rule_engine.detect(combined_data)

    return detection