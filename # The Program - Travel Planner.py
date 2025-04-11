# The Program - Travel Planner
import datetime
# Date input with validation
def get_date(prompt):
    while True:
        try:
            return datetime.datetime.strptime(input(f"{prompt} (YYYY-MM-DD): "), "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Try again.")
# --- Choice Menus ---
food_options = ["Vegetarian", "Local Cuisine", "Fine Dining", "Street Food"]
activity_options = ["Adventure", "Cultural", "Relaxation", "Nightlife"]
weather_options = ["Sunny", "Rainy", "Cold", "Mixed"]
destination_types = ["Beach", "Mountains", "Urban City", "Countryside"]
# Added food choice with statements with enumerate funcion (loops and index combined into one function)
print("Food Preferences:")
for i, f in enumerate(food_options, 1): print(f"{i}. {f}")
print(f"{len(food_options)+1}. Enter your own")
food_choice = input("Your choice: ")
food = food_options[int(food_choice)-1] if food_choice.isdigit() and 1 <= int(food_choice) <= len(food_options) else input("Enter your custom food: ")
# added activity preferencs with enumerate functions 
print("Activity Preferences:")
for i, a in enumerate(activity_options, 1): print(f"{i}. {a}")
print(f"{len(activity_options)+1}. Enter your own")
activity_choice = input("Your choice: ")
activity = activity_options[int(activity_choice)-1] if activity_choice.isdigit() and 1 <= int(activity_choice) <= len(activity_options) else input("Enter your custom activity: ")
print("Weather Forecast:")
for i, w in enumerate(weather_options, 1): print(f"{i}. {w}")
print(f"{len(weather_options)+1}. Enter your own")
weather_choice = input("Your choice: ")
weather = weather_options[int(weather_choice)-1] if weather_choice.isdigit() and 1 <= int(weather_choice) <= len(weather_options) else input("Enter custom weather: ")

print("Destination Type:")
for i, d in enumerate(destination_types, 1): print(f"{i}. {d}")
print(f"{len(destination_types)+1}. Enter your own")
dest_type_choice = input("Your choice: ")
dest_type = destination_types[int(dest_type_choice)-1] if dest_type_choice.isdigit() and 1 <= int(dest_type_choice) <= len(destination_types) else input("Enter custom destination type: ")