
RATES = {"bike": 10, "car": 30, "truck": 60}


def minutes_parked(times):
    try:
        if not isinstance(times, str):
            return 0

        parts = times.split('-')

        if len(parts) != 2:
            return 0

        entry, exit_time = parts

        def convert_time(t):
            h, m = t.strip().split(':')

            hour = int(h)
            minute = int(m)

            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Invalid time")

            return hour * 60 + minute

        start = convert_time(entry)
        end = convert_time(exit_time)

        duration = end - start

        if duration < 0:
            return 0

        return duration

    except (ValueError, AttributeError, TypeError):
        return 0


def hourly_rate(vehicle):
    if not isinstance(vehicle, str):
        return 0

    vehicle = vehicle.strip().lower()

    return RATES.get(vehicle, 0)


def format_plate(plate):
    if not isinstance(plate, str):
        return ""

    p = plate.strip().upper()

    if len(p) != 10 or not p.isalnum():
        return ""

    return p[0] + p[1] + " " + p[2:4] + " " + p[4:6] + " " + p[6:10]


def main():
    print("==== Running minutes_parked ====")
    user_input = input("Enter entry and exit time (e.g. 09:30-11:45): ")
    result = minutes_parked(user_input)
    print("Minutes Parked:", result)

    print("\n==== Running hourly_rate ====")
    user_input = input("Enter vehicle type (bike/car/truck): ")
    result = hourly_rate(user_input)
    print("Hourly Rate:", result)

    print("\n==== Running format_plate ====")
    user_input = input("Enter a number plate (e.g. ka01ab1234): ")
    result = format_plate(user_input)
    print("Formatted Plate:", result)


if __name__ == "__main__":
    main()
