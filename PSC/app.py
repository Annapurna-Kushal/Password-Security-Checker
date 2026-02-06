from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    """
    Check the strength of a password and return a score and feedback.
    """
    score = 0
    feedback = []
    suggestions = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
        suggestions.append("💡 Idea: Use a longer passphrase. For example, combine 3-4 random words like 'BlueMoon$Coffee42'")
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")
        suggestions.append("💡 Idea: Capitalize some words. Change 'password' to 'PassWord' to start.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")
        suggestions.append("💡 Idea: Include lowercase letters. Mix uppercase with lowercase like 'PaSsWoRd'.")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers (0-9)")
        suggestions.append("💡 Idea: Replace letters with numbers. Change 'E' to '3' or 'A' to '4', like 'P4ssw0rd'.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&*)")
        suggestions.append("💡 Idea: Add symbols like !@#$%^&*. Try 'P@ssw0rd!' or 'MyPwd#2024'.")
    
    # Determine strength level
    if score <= 2:
        strength = "Weak"
        color = "#e74c3c"
    elif score <= 4:
        strength = "Fair"
        color = "#f39c12"
    elif score <= 6:
        strength = "Good"
        color = "#f1c40f"
    else:
        strength = "Strong"
        color = "#27ae60"
    
    return {
        "score": score,
        "max_score": 7,
        "strength": strength,
        "color": color,
        "feedback": feedback,
        "suggestions": suggestions
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check-password', methods=['POST'])
def check_password_api():
    data = request.get_json()
    password = data.get('password', '')
    
    if not password:
        return jsonify({"error": "Password is required"}), 400
    
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
