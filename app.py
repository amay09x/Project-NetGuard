from flask import Flask, render_template, request
from parser import LogParser
from analyzer import ThreatDetector
from visualizer import GraphMaker
import os

# 1. ALWAYS CREATE THE APP OBJECT FIRST
app = Flask(__name__)

# 2. USE THE /tmp DIRECTORY FOR CLOUD DEPLOYMENT
# Vercel is read-only; /tmp is the only place we can save files
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    threats = {}
    if request.method == 'POST':
        file = request.files['logfile']
        if file.filename != '':
            # Save the file to /tmp instead of uploads/
            filepath = os.path.join(UPLOAD_FOLDER, 'uploaded_server.log')
            file.save(filepath)

            parser = LogParser(filepath)
            clean_data = parser.read_logs()

            detector = ThreatDetector(clean_data)
            threats = detector.find_threats()

            # Tell visualizer to save the graph to /tmp
            visuals = GraphMaker(threats)
            visuals.plot_top_threats()

            return render_template('index.html', threats=threats, uploaded=True)

    return render_template('index.html', threats={}, uploaded=False)

# 3. FOR VERCEL TO FIND YOUR APP
app = app

if __name__ == '__main__':
    app.run(debug=True)
