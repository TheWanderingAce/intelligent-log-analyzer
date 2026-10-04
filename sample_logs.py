import os

os.makedirs("sample_logs", exist_ok=True)
with open("sample_logs/server.log", "w") as file: 
    #Writing sample error logs to test
    file.write("2026-10-04 12:00:05 ERROR Database connection timeout\n")
    file.write("2026-10-04 12:05:10 WARNING Disk usage above 80%\n")
    file.write("2026-10-04 12:10:15 INFO Server restarted successfully\n")
    file.write("2026-10-04 12:15:20 ERROR Failed to deploy application\n")
    print("wrote sample logs successfully")