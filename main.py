import requests
import matplotlib.pyplot as plt
from config import API_KEY, CITY, UNITS


def fetch_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={CITY}&appid={API_KEY}&units={UNITS}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data.")
        print(response.json())
        return None

    return response.json()


def display_weather(data):
    print("\n========== WEATHER REPORT ==========")
    print(f"City        : {data['name']}")
    print(f"Weather     : {data['weather'][0]['main']}")
    print(f"Description : {data['weather'][0]['description'].title()}")
    print(f"Temperature : {data['main']['temp']} °C")
    print(f"Humidity    : {data['main']['humidity']} %")
    print(f"Pressure    : {data['main']['pressure']} hPa")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")
    print("====================================")


def visualize(data):
    labels = [
        "Temperature",
        "Humidity",
        "Pressure",
        "Wind Speed"
    ]

    values = [
        data["main"]["temp"],
        data["main"]["humidity"],
        data["main"]["pressure"],
        data["wind"]["speed"]
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    bars = ax.bar(labels, values)

    ax.set_title("Weather Dashboard")
    ax.set_ylabel("Values")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1f}",
            ha="center"
        )

    plt.tight_layout()
    plt.show()


def main():
    data = fetch_weather()

    if data:
        display_weather(data)
        visualize(data)


if __name__ == "__main__":
    main()