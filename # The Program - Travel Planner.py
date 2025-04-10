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
