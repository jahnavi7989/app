from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home route: Handles user input of test string and regex
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex")

        # Perform regex matching
        try:
            matches = re.findall(regex_pattern, test_string)
        except re.error:
            matches = ["Invalid Regex Pattern"]

        return render_template("index.html", matches=matches, test_string=test_string, regex=regex_pattern)
    return render_template("index.html", matches=[], test_string="", regex="")

# Route to validate email input
@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form.get("email")
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    is_valid = re.match(email_pattern, email) is not None
    message = f"'{email}' is a valid email" if is_valid else f"'{email}' is NOT a valid email"
    return render_template("validate.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
