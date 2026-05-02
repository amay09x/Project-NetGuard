# NetGuard: Network Traffic & Threat Log Analyzer 🛡️

**NetGuard** is a security-focused data analysis tool designed to parse server logs and identify potential cyber threats in real-time. Built as a part of the Semester 2 CSE (AI & ML) curriculum, this application utilizes the full Python data science stack to transform raw text logs into actionable visual insights.



## 🚀 Key Features
* **Automated Log Ingestion:** Efficiently reads and cleans raw `.log` or `.csv` server files.
* **Threat Classification:** Uses custom logic to identify:
    * **Brute Force Attacks:** Flagged based on repeated 401 (Unauthorized) status codes.
    * **DDoS / API Spam:** Flagged based on high-frequency 429 (Too Many Requests) codes.
* **Interactive Dashboard:** A web-based interface for uploading logs and viewing results.
* **Visual Reporting:** Generates dynamic bar charts to visualize attack intensity per IP.

## 🛠️ Technology Stack
| Technology | Implementation |
| :--- | :--- |
| **Python** | Core application logic and flow. |
| **OOPS** | Modular classes for Parsing, Analyzing, and Visualizing. |
| **File Handling** | Reading raw server data and temporary file storage. |
| **Pandas** | Data manipulation and grouping by IP address. |
| **NumPy** | Numerical operations and frequency calculations. |
| **Matplotlib** | Generation of threat-intensity graphs. |
| **Flask** | Web framework for the user interface and file upload system. |

## 📂 Project Structure
```text
NetGuard/
│
├── app.py              # Main Flask application & routes
├── parser.py           # OOPS class for log file ingestion
├── analyzer.py         # Logic for threat detection (Pandas/NumPy)
├── visualizer.py       # Graph generation logic (Matplotlib)
├── log                 # Sample log file for testing
├── static/             # Folder for generated threat charts
└── templates/          # Folder for HTML frontend
    └── index.html      # The Dashboard UI

## 🔧 Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/amay09x/Project-NetGuard.git
   ```
2. **Install dependencies:**
   ```bash
   pip install flask pandas numpy matplotlib
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Access the Dashboard:** Open `[http://127.0.0.1:5000](http://127.0.0.1:5000)` in your browser and upload the provided `log` file to see the analysis.

## 📝 Future Scope (AI & ML)
As AI & ML students, we plan to extend this project by implementing:
1. **Anomaly Detection:** Using Scikit-Learn to detect "zero-day" threats that don't follow standard patterns.
2. **Predictive Blocking:** Forecasting potential attacks before they hit the server based on historical traffic trends.

**Note:** This project was developed as part of the ByteXL / CU training program for 2nd-semester students.
```
