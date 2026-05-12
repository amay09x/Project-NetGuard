import matplotlib.pyplot as plt
import os

class GraphMaker:
    def __init__(self, threat_data):
        self.threat_data = threat_data

    def plot_top_threats(self):
        # create static folder for flask images if it doesn't exist
        if not os.path.exists('static'):
            os.makedirs('static')

        if not self.threat_data:
            print("No threats to plot.")
            return

        # Extract IPs for X-axis 
        ips = list(self.threat_data.keys())
        
        # THIS IS THE MAGIC LINE THAT FIXES YOUR ERROR:
        # It digs into the dictionary and pulls out ONLY the 'count' number for the graph
        counts = [data['count'] for data in self.threat_data.values()]

        # build the bar chart
        plt.figure(figsize=(8, 5))
        plt.bar(ips, counts, color='red')
        plt.xlabel('Suspicious IPs')
        plt.ylabel('Number of Bad Requests')
        plt.title('Top Network Threats Detected')
        
        # save the image inside the static folder for flask
        plt.savefig('static/threat_report.png')
        plt.close()
