from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days
new_date = current_date - timedelta(days=5)

# Print the result
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date after subtracting five days:", new_date.strftime("%Y-%m-%d"))