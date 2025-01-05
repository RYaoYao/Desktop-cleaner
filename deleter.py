import os
from datetime import datetime, timedelta
downloads_path = os.path.expanduser(r"~/Downloads")

cutoff_date = datetime.now() - timedelta(days=750)
cutoff_timestamp = cutoff_date.timestamp()  

for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path,file_name)
    if os.path.isfile(file_path) and file_name.lower().endswith(('.txt', '.jpg')):
        modified_date = os.path.getmtime(file_path)
        print(modified_date,file_name)
        if modified_date < cutoff_timestamp:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

