def compute_fare(distance):
    min_fare = 12
    base_distance = 8
    additional_fare_per_km = 3

    if distance <= 0:
        return "Invalid distance. Distance must be greater than 0."
    if distance <= base_distance:
        total_fare = min_fare
    else:
        additional_distance = distance - base_distance
        total_fare = min_fare + (additional_distance * additional_fare_per_km)

    return total_fare


def compute_discounted_fare(distance, passenger_category):
    discount_rates = {
        "regular": 0,
        "student": 0.20,
        "pwd": 0.35,
    }

    if passenger_category not in discount_rates:
        return "Invalid passenger category. Choose from 'regular', 'student', or 'pwd'."

    fare = compute_fare(distance)
    if isinstance(fare, str):
        return fare

    discount_rate = discount_rates[passenger_category]
    discounted_fare = fare * (1 - discount_rate)
    return discounted_fare



distance = float(input("Enter the distance traveled (in kilometers): "))


if distance <= 0:
    print("Invalid distance. Distance must be greater than 0.")
else:

    while True:
        passenger_category = input("Enter the passenger category (regular, student, pwd): ").lower()
        fare = compute_discounted_fare(distance, passenger_category)
        if isinstance(fare, str) and "Invalid passenger category" in fare:
            print(fare)
        else:
            break

    print(f'The fare for travelling {distance:.2f} kilometers as a {passenger_category} passenger is {fare:.2f} pesos.')
