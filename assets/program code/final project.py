#Name- Gbenga Olusehin
#Final Project

# Briefing on training program

print("welcome to North Lincolnshire Judo")
print("Only Intermediate and Elite athletes can enter competitions")
print("Competitions are held on the second Saturday of each month")
print("Athletes can receive a maximum of five hours private coaching a week")


# Setup and Initial Variables Define the price structure and
#weight categories as global constants for easy reference and modification.

TRAINING_PLAN_PRICES = {
    'Beginner': 25.00,
    'Intermediate': 30.00,
    'Elite': 35.00
}
PRIVATE_TUITION_PRICE_PER_HOUR = 9.50
COMPETITION_ENTRY_FEE = 22.00
WEIGHT_CATEGORIES = {
    'Heavyweight': float('inf'),  # Represents no upper limit
    'Light-Heavyweight': 100,
    'Middleweight': 90,
    'Light-Middleweight': 81,
    'Lightweight': 73,
    'Flyweight': 66
}

#Input Gathering Function Create a function to gather and validate input for each athlete.
#This includes handling invalid data for training plans and weight categories and ensuring numerical inputs are indeed numbers.

def get_athlete_info():
    name = input("\nAthlete name: ")
    
    while True:
        training_plan = input("Training plan (Beginner/Intermediate/Elite): ")
        if training_plan not in TRAINING_PLAN_PRICES:
            print("Invalid training plan. Please choose Beginner, Intermediate, or Elite.")
            continue
        break
    
    current_weight = float(input("Current weight (kg): "))
    
    while True:
        competition_weight_category = input("Competition weight category (Flyweight, Lightweight, Light-Middleweight, Middleweight, Light-Heavyweight, Heavyweight): ")
        if competition_weight_category not in WEIGHT_CATEGORIES:
            print("Invalid weight category. Please enter a valid category.")
            continue
        break
    
    num_competitions = int(input("Number of competitions entered this month: "))
    
    while True:
        private_coaching_hours = int(input("Number of hours private coaching (0-5): "))
        if not 0 <= private_coaching_hours <= 5:
            print("Invalid number of hours. Please enter a value between 0 and 5.")
            continue
        break

    return name, training_plan, current_weight, competition_weight_category, num_competitions, private_coaching_hours

#Function to Cost Calculation and Weight Comparison


def calculate_total_cost(training_plan, num_competitions, private_coaching_hours):
    weekly_fee = TRAINING_PLAN_PRICES[training_plan]
    total_cost = weekly_fee * 4  # 4 weeks in a month
    
    if private_coaching_hours > 0:
        total_cost += private_coaching_hours * PRIVATE_TUITION_PRICE_PER_HOUR * 4
    
    if training_plan in ['Intermediate', 'Elite']:
        total_cost += num_competitions * COMPETITION_ENTRY_FEE
    
    return total_cost
def compare_weight(current_weight, competition_weight_category):
    upper_limit = WEIGHT_CATEGORIES[competition_weight_category]
    if current_weight > upper_limit:
        return f"Over the weight limit for {competition_weight_category}."
    else:
        return f"Within the weight limit for {competition_weight_category}."

# Main Program Function to Loop. Let's put it all together into a main loop that accepts new athletes until the user decides to stop.
#It will integrate error handling for user inputs and utilize the previously defined functions.

def main():
    while True:
        try:
            athlete_info = get_athlete_info()
            total_cost = calculate_total_cost(athlete_info[1], athlete_info[4], athlete_info[5])
            weight_comparison = compare_weight(athlete_info[2], athlete_info[3])
            
            print("\nAthlete Information:")
            print(f"Athlete Name: {athlete_info[0]}")
            print(f"Training Plan: {athlete_info[1]}")
            print(f"Current Weight: {athlete_info[2]} kg")
            print(f"Competition Weight Category: {athlete_info[3]}")
            print(f"Number of Competitions: {athlete_info[4]}")
            print(f"Private Coaching Hours: {athlete_info[5]}")
            print("\nCost and Weight Comparison:")
            print(f"Total Monthly Cost: £{total_cost:.2f}")
            print(weight_comparison)
            
            another = input("\nRegister another athlete? (yes/no): ")
            if another.lower() != 'yes':
                break
        except ValueError as e:
            print("Invalid input, please enter the correct data types.")
        except Exception as e:
            print("An unexpected error occurred. Please try again.")

# Run the program
if __name__ == "__main__":
    main()    
