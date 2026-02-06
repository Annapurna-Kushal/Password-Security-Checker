# Password Strength Checker

A simple web application that checks the strength of passwords and provides real-time feedback on how to improve them.

## Features

- **Real-time Password Analysis**: Get instant feedback as you type
- **Visual Strength Indicator**: Color-coded strength bar showing password quality
- **Detailed Feedback**: Suggestions for improving password strength
- **Show/Hide Password**: Toggle password visibility
- **Responsive Design**: Works on desktop and mobile devices

## Password Strength Criteria

The password strength checker evaluates passwords based on:

1. **Length**
   - 8+ characters: +1 point
   - 12+ characters: +1 point
   - 16+ characters: +1 point

2. **Character Types**
   - Contains uppercase letters (A-Z): +1 point
   - Contains lowercase letters (a-z): +1 point
   - Contains numbers (0-9): +1 point
   - Contains special characters (!@#$%^&*): +1 point

### Strength Levels

- **Weak** (Score 0-2): Needs significant improvement
- **Fair** (Score 3-4): Acceptable but could be stronger
- **Good** (Score 5-6): Strong password
- **Strong** (Score 7): Excellent password, very secure

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download this repository:
```bash
cd your-project-directory
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter a password in the input field and see the strength analysis in real-time.

## Project Structure

```
password-strength-checker/
├── app.py              # Flask application and password checking logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML template for the web interface
├── static/
│   └── style.css       # CSS styling for the application
└── README.md           # This file
```

## Usage

1. Navigate to the application in your browser
2. Type a password in the input field
3. View the real-time strengths analysis:
   - Color-coded strength bar
   - Strength level (Weak, Fair, Good, Strong)
   - Score out of 7
   - Specific suggestions for improvement

4. Use the "Show/Hide" button to toggle password visibility

## API Endpoints

### POST /api/check-password

Check the strength of a password.

**Request Body:**
```json
{
  "password": "your_password_here"
}
```

**Response:**
```json
{
  "score": 5,
  "max_score": 7,
  "strength": "Good",
  "color": "#f1c40f",
  "feedback": [
    "Add special characters (!@#$%^&*)"
  ]
}
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: CSS3 with gradients and animations

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Future Enhancements

- Password breach checking against known compromised passwords
- Entropy calculation
- Password generation suggestions
- Support for multiple languages
- Dark mode theme
- Password history tracking

---

**Note**: This tool is for educational purposes. Always follow your organization's password policies and security guidelines.
