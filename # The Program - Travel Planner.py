import datetime  # Used for handling dates
import openai  # Used for accessing the OpenAI API (ChatGPT)
openai.api_key = "ENTER API KEY HERE"  # <-- Replace with your OpenAI API key

# This program makes use of try/except blocks to handle errors
# It includes ChatGPT integration for generating local travel tips
# It uses numerical options for easier menu selection

print("Welcome to VoyageGenie, Your AI Travel Planner!")

try:
    # Get destination input from the user
    destination = input("Enter destination (city, country): ")

    # Get trip start date with input validation
    while True:
        try:
            start = datetime.datetime.strptime(input("Trip start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Try again.")

    # Get trip end date with input validation and logical check
    while True:
        try:
            end = datetime.datetime.strptime(input("Trip end date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            if end <= start:
                print("End date must be after start date.")  # Ensure end date is after start date
            else:
                break
        except ValueError:
            print("Invalid date format. Try again.")

    # Get food preference from a menu or custom input
    print("\nFood Preferences:")
    print("1. Vegetarian\n2. Local Cuisine\n3. Fine Dining\n4. Street Food\n5. Enter your own")
    choice = input("Choose an option: ")
    food = ["Vegetarian", "Local Cuisine", "Fine Dining", "Street Food"]
    food = food[int(choice)-1] if choice in "1234" else input("Enter your food preference: ")

    # Get activity preference from a menu or custom input
    print("\nActivity Preferences:")
    print("1. Adventure\n2. Cultural\n3. Relaxation\n4. Nightlife\n5. Enter your own")
    choice = input("Choose an option: ")
    activity = ["Adventure", "Cultural", "Relaxation", "Nightlife"]
    activity = activity[int(choice)-1] if choice in "1234" else input("Enter your activity preference: ")

    # Get weather preference from a menu or custom input
    print("\nWeather Forecast:")
    print("1. Sunny\n2. Rainy\n3. Cold\n4. Mixed\n5. Enter your own")
    choice = input("Choose an option: ")
    weather = ["Sunny", "Rainy", "Cold", "Mixed"]
    weather = weather[int(choice)-1] if choice in "1234" else input("Enter the expected weather: ")

    # Get destination type from a menu or custom input
    print("\nDestination Type:")
    print("1. Beach\n2. Mountains\n3. Urban City\n4. Countryside\n5. Enter your own")
    choice = input("Choose an option: ")
    dest_type = ["Beach", "Mountains", "Urban City", "Countryside"]
    dest_type = dest_type[int(choice)-1] if choice in "1234" else input("Enter your destination type: ")

    # Generate clothing suggestions based on weather
    clothes = {
        "Sunny": ["sunhat", "sunglasses", "light clothes"],
        "Rainy": ["umbrella", "raincoat", "waterproof shoes"],
        "Cold": ["coat", "gloves", "scarf"],
        "Mixed": ["layered clothes", "light jacket"]
    }.get(weather, ["basic clothing"])  # Default clothing if weather not recognized

    # Generate basic itinerary for the trip
    itinerary = [
        f"{start}: Arrive in {destination} and explore nearby areas.",
        f"Middle of trip: Enjoy {activity.lower()} experiences.",
        f"{end}: Final day and enjoy a nice {food.lower()} meal."
    ]

    # Prepare a packing list based on travel essentials and activity
    packing_list = ["passport", "toiletries", "ID"] + clothes + [f"{activity.lower()} gear"]

    # ChatGPT Integration for Local Tips
    try:
        # Create a prompt for ChatGPT to generate travel tips based on user preferences
        chat_prompt = (
            f"You're a travel expert. Give some detailed, practical travel tips for visiting {destination}. "
            f"The traveler enjoys {activity.lower()} activities and prefers {food.lower()} food. "
            f"Tips should be helpful, fun, and insightful."
        )

        # Call OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,  # Slight creativity in responses
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": chat_prompt}
            ]
        )

        # Parse and format ChatGPT's response
        content = response["choices"][0]["message"]["content"]
        tips = content.strip().split("\n")  # Split tips into a list

    except Exception as e:
        # Fallback tips if ChatGPT fails
        print("\n[!] Could not retrieve tips from ChatGPT:", e)
        tips = [
            f"Explore local {food.lower()} options in {destination}.",
            "Learn basic greetings and respect local customs."
        ]

    # Final Output Section: Display compiled travel plan
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

# Outer exception catch for any unforeseen errors
except Exception as e:
    print("\n[!] Something went wrong:", e)
