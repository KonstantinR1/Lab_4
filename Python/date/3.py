from datetime import datetime

# Get the current date and time with microseconds
current_datetime = datetime.now()

# Drop microseconds
datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print the results
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)