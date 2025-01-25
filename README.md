
# TourMate - Personalized Tour Recommendation System

TourMate is a web-based application that provides personalized tour recommendations based on user preferences. The app leverages collaborative filtering and cosine similarity techniques to recommend the best tours to users, making travel planning easier and more enjoyable.

---

## Features

- **Personalized Recommendations**: Enter your user ID to get tour recommendations tailored to your preferences.
- **Tour Details**: Includes information about the destination, state, type, popularity, and the best time to visit.
- **User Interface**: Clean and attractive design using Bootstrap for a seamless user experience.
- **Efficient Recommendation Engine**: Uses collaborative filtering and cosine similarity to calculate the best recommendations.
- **Responsive Design**: Fully responsive and optimized for both desktop and mobile devices.

---

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap)
- **Libraries**:
  - **Pandas** for data handling and manipulation
  - **NumPy** for numerical operations
  - **scikit-learn** for calculating cosine similarity
  - **Matplotlib** and **Seaborn** for data visualization
- **Database**: CSV files (for simplicity in this prototype)
  
---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/BhumikaTechHub/TourMate.git
cd TourMate
```
### 2. Install the required dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install required packages:
```
pip install -r requirements.txt
```

### 3. Run the Flask application
```bash
python app.py
```


