print("Intelligent Log Analyzer")

file_path = "sample_logs/server.log"

try:
    with open(file_path,"r") as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())
except FileNotFoundError:
    print("The server log file was not found.")