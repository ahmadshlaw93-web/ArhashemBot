from flask import Flask, request

app = Flask(__name__)

STUDENTS = {
    "1742112455": {
        "name": "Sahareh Elahi",
        "class": "12",
        "field": "Experimental"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        national_id = request.form.get("national_id", "").strip()
        student = STUDENTS.get(national_id)

        if student:
            message = f"""
            <hr>
            <h3>Student Found</h3>
            <p>Name: {student["name"]}</p>
            <p>Class: {student["class"]}</p>
            <p>Field: {student["field"]}</p>

            <form method="POST" action="/confirm">
                <input type="hidden" name="national_id" value="{national_id}">
                <button type="submit">Confirm - This is my child</button>
            </form>
            """
        else:
            message = "<hr><p>Student not found.</p>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Arhashem</title>
    </head>
    <body>
        <h2>Arhashem - Family Connection</h2>

        <form method="POST">
            <label>National ID:</label><br>
            <input type="text" name="national_id" required>
            <br><br>
            <button type="submit">Search Student</button>
        </form>

        {message}
    </body>
    </html>
    """

@app.route("/confirm", methods=["POST"])
def confirm():
    national_id = request.form.get("national_id", "").strip()
    student = STUDENTS.get(national_id)

    if not student:
        return "Student not found", 404

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Arhashem</title>
    </head>
    <body>
        <h2>Connection Successful</h2>
        <p>Student: {student["name"]}</p>
        <p>Family connection registered successfully.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)