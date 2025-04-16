import datetime
import openai
openai.api_key = "ENTER API KEY HERE"

# This program makes use of try/except blocks to help with error handling
# This program includes chatgpt integration for the portion that involves the itinerary
# This program is also using /nx to denote numbers for options 

print("Welcome to VoyageGenie, Your AI Travel Planner!")

try:
    destination = input("Enter destination (city, country): ")

    while True:
        try:
            start = datetime.datetime.strptime(input("Trip start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Try again.")

    while True:
        try:
            end = datetime.datetime.strptime(input("Trip end date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            if end <= start:
                print("End date must be after start date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Try again.")

    print("\nFood Preferences:")
    print("1. Vegetarian\n2. Local Cuisine\n3. Fine Dining\n4. Street Food\n5. Enter your own")
    choice = input("Choose an option: ")
    food = ["Vegetarian", "Local Cuisine", "Fine Dining", "Street Food"]
    food = food[int(choice)-1] if choice in "1234" else input("Enter your food preference: ")

    print("\nActivity Preferences:")
    print("1. Adventure\n2. Cultural\n3. Relaxation\n4. Nightlife\n5. Enter your own")
    choice = input("Choose an option: ")
    activity = ["Adventure", "Cultural", "Relaxation", "Nightlife"]
    activity = activity[int(choice)-1] if choice in "1234" else input("Enter your activity preference: ")

    print("\nWeather Forecast:")
    print("1. Sunny\n2. Rainy\n3. Cold\n4. Mixed\n5. Enter your own")
    choice = input("Choose an option: ")
    weather = ["Sunny", "Rainy", "Cold", "Mixed"]
    weather = weather[int(choice)-1] if choice in "1234" else input("Enter the expected weather: ")

    print("\nDestination Type:")
    print("1. Beach\n2. Mountains\n3. Urban City\n4. Countryside\n5. Enter your own")
    choice = input("Choose an option: ")
    dest_type = ["Beach", "Mountains", "Urban City", "Countryside"]
    dest_type = dest_type[int(choice)-1] if choice in "1234" else input("Enter your destination type: ")

    # Clothing Suggestions
    clothes = {
        "Sunny": ["sunhat", "sunglasses", "light clothes"],
        "Rainy": ["umbrella", "raincoat", "waterproof shoes"],
        "Cold": ["coat", "gloves", "scarf"],
        "Mixed": ["layered clothes", "light jacket"]
    }.get(weather, ["basic clothing"])

    # Itinerary
    itinerary = [
        f"{start}: Arrive in {destination} and explore nearby areas.",
        f"Middle of trip: Enjoy {activity.lower()} experiences.",
        f"{end}: Final day and enjoy a nice {food.lower()} meal."
    ]

    # Packing List
    packing_list = ["passport", "toiletries", "ID"] + clothes + [f"{activity.lower()} gear"]

    # 💬 ChatGPT Tips
    try:
        chat_prompt = (
            f"You're a travel expert. Give some detailed, practical travel tips for visiting {destination}. "
            f"The traveler enjoys {activity.lower()} activities and prefers {food.lower()} food. "
            f"Tips should be helpful, fun, and insightful."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": chat_prompt}
            ]
        )

        # ✅ Print full response content
        content = response["choices"][0]["message"]["content"]
        tips = content.strip().split("\n")

    except Exception as e:
        print("\n[!] Could not retrieve tips from ChatGPT:", e)
        tips = [
            f"Explore local {food.lower()} options in {destination}.",
            "Learn basic greetings and respect local customs."
        ]

    # 🧾 Final Output
    print("\n🧳 Your VoyageGenie Travel Plan is Ready!\n")
    print("🌤️ Weather:", weather)

    print("\n👕 Clothing Suggestions:")
    for item in clothes:
        print("-", item)

    print("\n📅 Itinerary:")
    for day in itinerary:
        print("-", day)

    print("\n🎒 Packing List:")
    for item in packing_list:
        print("-", item)

    print("\n🌍 Local Tips from ChatGPT:")
    for tip in tips:
        print("-", tip)

except Exception as e:
    print("\n[!] Something went wrong:", e)
