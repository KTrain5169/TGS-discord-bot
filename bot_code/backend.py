def handle_ping_command(latency):
    latency_ms = round(latency * 1000)  # Convert latency to milliseconds
    return f"Pong! 🏓 Latency: {latency_ms}ms"
