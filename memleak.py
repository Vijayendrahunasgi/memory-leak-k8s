# app.py
import time
from prometheus_client import start_http_server, Gauge
# Optional app-level metric to track “allocated bytes” for demo
LEAK_BYTES = Gauge('app_leak_bytes', 'Simulated leaked bytes')

buf = []
def leak():
    total = 0
    while True:
        chunk = b"x" * (10 * 1024 * 1024)  # 10MB
        buf.append(chunk)
        total += len(chunk)
        LEAK_BYTES.set(total)
        print(f"Leaked ~{total/1024/1024:.0f}MB")
        time.sleep(5)

if __name__ == "__main__":
    # Start a metrics server on port 8000 at /metrics
    start_http_server(8000)
    leak()
