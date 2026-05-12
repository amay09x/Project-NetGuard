from flask import Flask, render_template, request
from parser import LogParser
from analyzer import ThreatDetector
from visualizer import GraphMaker
# Update these lines in app.py
import os

UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# initialize flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    threats = {}
    
    # If the user clicks the "Analyze File" button
    if request.method == 'POST':
        # Get the file from the HTML form
        file = request.files['logfile']
        
        if file.filename != '':
            # Save the file temporarily
            filepath = os.path.join('uploads', 'uploaded_server.log')
            file.save(filepath)

            # 1. read logs from the newly uploaded file
            parser = LogParser(filepath)
            clean_data = parser.read_logs()

            # 2. find threats
            detector = ThreatDetector(clean_data)
            threats = detector.find_threats()

            # 3. draw graphs
            visuals = GraphMaker(threats)
            visuals.plot_top_threats()

            # 4. send data to webpage (we pass 'uploaded=True' so the HTML knows to show the results)
            return render_template('index.html', threats=threats, uploaded=True)

    # If the user just opened the page for the first time (GET request)
    return render_template('index.html', threats={}, uploaded=False)

if __name__ == '__main__':
    app.run(debug=True)
app = app
