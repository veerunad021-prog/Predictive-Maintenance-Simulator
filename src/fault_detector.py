def detect_faults(data):

    faults = []

    if data["temperature"] > 80:
        faults.append("OVER TEMPERATURE")

    if data["vibration"] > 6:
        faults.append("EXCESSIVE VIBRATION")

    if data["current"] > 8:
        faults.append("OVER CURRENT")

    if data["rpm"] < 1200:
        faults.append("LOW RPM")

    if data["rpm"] > 1700:
        faults.append("EXCESSIVE RPM")

    return faults