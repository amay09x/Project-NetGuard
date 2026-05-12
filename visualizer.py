import matplotlib.pyplot as plt
import os

class GraphMaker:
    def __init__(self, threat_data):
        self.threat_data = threat_data

    def plot_top_threats(self):
        # REMOVE the os.path.exists and os.makedirs lines from here!
        
        if not self.threat_data:
            print("No threats to plot.")
            return

        ips = list(self.threat_data.keys())
        counts = [data['count'] for data in self.threat_data.values()]

        plt.figure(figsize=(8, 5))
        plt.bar(ips, counts, color='red')
        plt.xlabel('Suspicious IPs')
        plt.ylabel('Number of Bad Requests')
        plt.title('Top Network Threats Detected')
        
        # Save to /tmp as you already have, but ensure no folder creation logic remains
        plt.savefig('/tmp/threat_report.png')
        plt.close()
