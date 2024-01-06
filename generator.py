import matplotlib.pyplot as plt

def get_hours_spent():
    life_units = {
        "Significant other": "Time spent with partner, dates, quality time",
        "Family": "Engaging with kids, parents, siblings, family activities",
        "Friendship": "Time dedicated to friends, outings, conversations",
        "Physical Health/Sports": "Exercise, workouts, physical therapy",
        "Mental Health/Mindfulness": "Therapy, meditation, self-care practices",
        "Spirituality/Faith": "Religious practices, spiritual gatherings",
        "Community/Citizenship": "Participation in local clubs, neighborhood initiatives",
        "Societal Engagement": "Volunteering, activism, supporting causes",
        "Job/Career": "Work hours, professional commitments",
        "Education/Learning": "Courses, training, self-improvement",
        "Finances": "Budgeting, investing, financial planning",
        "Hobbies/Interests": "Pursuing personal hobbies, recreational activities",
        "Online Entertainment": "Time spent on social media, gaming, watching videos",
        "Offline Entertainment": "Vacations, theater, live events",
        "Physiological Needs": "Eating, sleeping, intimacy, self-care routines",
        "Daily Routine": "Hygiene, household chores, commuting"
    }

    print("Welcome to the Life Prioritization Tool!\n")
    print("This tool helps you assess and visualize the distribution of your time,")
    print("importance, and satisfaction across various aspects of your life in a typical week.\n")
    print("Please enter the number of hours you spend on each life unit in a typical week,")
    print("and rank their importance and satisfaction on a scale of 1 to 10.\n")

    hours_spent = {}
    importance_rank = {}
    satisfaction_rank = {}
    for unit, description in life_units.items():
        print(f"\n{unit}:")
        
        # Validating hours spent
        while True:
            try:
                hours = float(input(f"How many hours do you spend on {unit} in a typical week? ({description}): "))
                if 0 <= hours <= 168:
                    hours_spent[unit] = hours
                    break
                else:
                    print("Hours spent must be between 0 and 168. Please enter a valid value.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")

        # Validating importance ranking
        while True:
            try:
                importance = int(input(f"On a scale of 1 to 10, how important is {unit} to you?: "))
                if 1 <= importance <= 10:
                    importance_rank[unit] = importance
                    break
                else:
                    print("Importance ranking must be between 1 and 10. Please enter a valid value.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")

        # Validating satisfaction ranking
        while True:
            try:
                satisfaction = int(input(f"On a scale of 1 to 10, how satisfied are you with your current situation regarding {unit}?: "))
                if 1 <= satisfaction <= 10:
                    satisfaction_rank[unit] = satisfaction
                    break
                else:
                    print("Satisfaction ranking must be between 1 and 10. Please enter a valid value.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")

    return hours_spent, importance_rank, satisfaction_rank

def calculate_total(hours_spent):
    total_hours = sum(hours_spent.values())
    return total_hours

def main():
    hours_spent, importance_rank, satisfaction_rank = get_hours_spent()
    total_hours = calculate_total(hours_spent)
    
    print("\nYour hours distribution in a typical week:")
    for unit, hours in hours_spent.items():
        print(f"- {unit}: {hours} hours")
    
    print("\nImportance ranking for each life unit:")
    for unit, rank in importance_rank.items():
        print(f"- {unit}: Importance rank {rank}/10")

    print("\nSatisfaction ranking for each life unit:")
    for unit, rank in satisfaction_rank.items():
        print(f"- {unit}: Satisfaction rank {rank}/10")

    print(f"\nTotal hours entered in a typical week: {total_hours} hours")
    print("Remember, there are 168 hours in a week.")

    # Creating a bubble chart
    x = list(importance_rank.values())
    y = list(satisfaction_rank.values())
    sizes = list(hours_spent.values())

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, s=sizes, alpha=0.5)
    plt.title('Importance vs. Satisfaction vs. Hours Spent')
    plt.xlabel('Importance Rating')
    plt.ylabel('Satisfaction Rating')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
