print("Intelligent Log Analyzer\n")

file_path = "sample_logs/server.log"
error_count = 0
highest_count = 0
mcerror_type = ""
errors = {}

errors["Example"] = 1



try:
    with open(file_path,"r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
                parts = line.split()
                error_message = " ".join(parts[3:])
                if error_message in errors:
                    errors[error_message] += 1
                else:
                    errors[error_message] = 1
            
except FileNotFoundError:
    print("The server log file was not found.")

for error, count in errors.items():
    if count > highest_count:
        highest_count = count
        mcerror_type = error

most_common_errors = []
for error, count in errors.items():
    if count == highest_count:
        most_common_errors.append(error)



print(f"There were a total of {error_count} errors.\n")

if len(most_common_errors) == 1:
    print(f"The most common error was {most_common_errors} and it occurred {highest_count} times")
elif len(most_common_errors) > 1:
    print(f"These were the most common errors and they occurred {highest_count} times:")
    for mce_list in most_common_errors:
        print(f"{mce_list}")