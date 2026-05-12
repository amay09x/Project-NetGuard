import os

class LogParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.parsed_data = []

    def read_logs(self):
        # check if file exists to avoid crashing
        if not os.path.exists(self.filepath):
            print("Error: Log file not found!")
            return []

        # open and read the file
        with open(self.filepath, 'r') as file:
            for line in file:
                parts = line.split()
                # make sure the line has enough data before extracting
                if len(parts) > 8:
                    ip = parts[0]
                    status_code = parts[8]
                    # save as a dictionary
                    self.parsed_data.append({'ip': ip, 'code': status_code})

        return self.parsed_data