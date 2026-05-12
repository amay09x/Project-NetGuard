import pandas as pd
import numpy as np

class ThreatDetector:
    def __init__(self, raw_data):
        self.df = pd.DataFrame(raw_data)
        
        if not self.df.empty:
            self.df['code'] = pd.to_numeric(self.df['code'])

    def find_threats(self):
        if self.df.empty:
            return {}

        brute_force = self.df[self.df['code'] == 401]
        bf_counts = brute_force.groupby('ip').size()

        spam = self.df[self.df['code'] == 429]
        spam_counts = spam.groupby('ip').size()

        threats = {}
        
        # Label 401 errors as Brute Force
        for ip, count in bf_counts.items():
            threats[ip] = {'count': count, 'type': 'Brute Force Attack'}
            
        # Label 429 errors as DDoS / Spam
        for ip, count in spam_counts.items():
            if ip in threats:
                # If an IP is doing BOTH attacks!
                threats[ip]['count'] += count
                threats[ip]['type'] = 'Multiple Threat Types' 
            else:
                threats[ip] = {'count': count, 'type': 'DDoS / API Spam'}

        return threats