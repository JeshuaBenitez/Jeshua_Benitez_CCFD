import requests

body = {
    "Time": 10000,
    "V1": 0.1, "V2": -0.2, "V3": 0.05, "V4": 0.0, "V5": -1.2,
    "V6": 0.3, "V7": -0.4, "V8": 0.2, "V9": 0.0, "V10": 0.1,
    "V11": -0.1, "V12": 0.0, "V13": 0.05, "V14": -0.02, "V15": 0.01,
    "V16": 0.0, "V17": -0.03, "V18": 0.02, "V19": 0.0, "V20": 0.0,
    "V21": 0.0, "V22": 0.0, "V23": 0.0, "V24": 0.0, "V25": 0.0,
    "V26": 0.0, "V27": 0.0, "V28": 0.0,
    "Amount": 123.45
}

r = requests.post("http://127.0.0.1:8000/score", json=body)
print("STATUS:", r.status_code)
print("RAW:", r.text)
if r.headers.get("content-type", "").startswith("application/json"):
    print("JSON:", r.json())

