# Open the dataset
with open("life-expectancy.csv") as file:
    # Skip the header
    next(file)

    # Initialize variables to track min and max life expectancy
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_record = None
    max_record = None

    # Initialize variables for user-specified year analysis
    year_data = {}
    
    for line in file:
        # Split the line by comma
        parts = line.strip().split(",")

        # Get the relevant data: country, year, and life expectancy
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # Check for minimum life expectancy
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_record = (country, year, life_expectancy)

        # Check for maximum life expectancy
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_record = (country, year, life_expectancy)

        # Collect data for user-specified year analysis
        if year not in year_data:
            year_data[year] = []
        year_data[year].append(life_expectancy)

# Display the overall results
print(f"Minimum life expectancy: {min_life_expectancy} (Country: {min_record[0]}, Year: {min_record[1]})")
print(f"Maximum life expectancy: {max_life_expectancy} (Country: {max_record[0]}, Year: {max_record[1]})")

# User-specified year analysis
user_year = int(input("\nEnter a year to analyze: ").strip())
if user_year in year_data:
    year_life_expectancies = year_data[user_year]
    avg_life_expectancy = sum(year_life_expectancies) / len(year_life_expectancies)
    min_year_life_expectancy = min(year_life_expectancies)
    max_year_life_expectancy = max(year_life_expectancies)

    print(f"\nFor the year {user_year}:")
    print(f"Average life expectancy: {avg_life_expectancy}")
    print(f"Minimum life expectancy: {min_year_life_expectancy}")
    print(f"Maximum life expectancy: {max_year_life_expectancy}")
else:
    print(f"\nNo data available for the year {user_year}.")
