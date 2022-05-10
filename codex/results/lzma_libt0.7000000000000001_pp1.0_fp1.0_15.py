import lzma
lzma.decompress(resp.read()).decode("utf-8")

url = "http://localhost:5000/api/v1/predict"
payload = {
    "date": "2020-07-01T00:00:00Z",
    "hpa_id": "hpa",
    "model_type": "ssm",
    "region": "uk",
    "state": "S",
    "timeseries": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
