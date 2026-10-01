def calculate_health(data):
    """
    Calculate machine health score and maintenance status.
    """

    score = 100

    # Temperature
    if data["temperature"] > 80:
        score -= 30
    elif data["temperature"] > 65:
        score -= 15

    # Vibration
    if data["vibration"] > 5:
        score -= 30
    elif data["vibration"] > 3:
        score -= 15

    # Current
    if data["current"] > 7:
        score -= 20
    elif data["current"] > 5.5:
        score -= 10

    # RPM
    if data["rpm"] < 1300:
        score -= 20
    elif data["rpm"] < 1400:
        score -= 10

    score = max(0, score)

    if score >= 80:
        status = "NORMAL"
        recommendation = "Continue normal operation"
    elif score >= 50:
        status = "WARNING"
        recommendation = "Schedule maintenance inspection"
    else:
        status = "CRITICAL"
        recommendation = "Stop machine and perform maintenance"

    return score, status, recommendation