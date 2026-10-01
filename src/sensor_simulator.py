import random


def generate_sensor_data(cycle):
    """Simulate gradual industrial motor degradation."""

    degradation = cycle * 1.2

    temperature = random.uniform(45, 52) + degradation
    vibration = random.uniform(1.0, 1.8) + (degradation * 0.12)
    current = random.uniform(3.5, 4.2) + (degradation * 0.08)
    rpm = random.uniform(1470, 1500) - (degradation * 3)

    return {
        "temperature": round(temperature, 2),
        "vibration": round(vibration, 2),
        "current": round(current, 2),
        "rpm": round(rpm, 2)
    }