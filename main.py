# main.py
# app.py
# In this file I will define my Flask application,
# the API endpoints, and the logic for interacting with my 'student_progress_db' from MySQL

from flask import Flask, request, jsonify
from db_utils import get_db_connection
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# API Endpoints

# 1. Get the count of students working on target
@app.route('/api/students/working_on_target', methods=['GET'])
def students_working_on_target():
    connection = get_db_connection(app)
    if not connection:
        return jsonify({'message': 'Database connection failed'}), 500

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS num_students_working_on_target FROM progress_reports WHERE feedback = 'Working on target'")
    results = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify(results)
# 2. Get progress report for a specific student i.e by id
@app.route('/api/student/<int:student_id>', methods=['GET'])
def get_student_progress(student_id):
    connection = get_db_connection(app)
    cursor = connection.cursor(dictionary=True)
    # SQL query to join students and progress_reports to retrieve data for a specific student
    cursor.execute("""
        SELECT s.first_name, s.last_name, p.subject, p.score, p.feedback, p.report_date
        FROM students s
        JOIN progress_reports p ON s.id = p.student_id
        WHERE s.id = %s
    """, (student_id,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    if results:
        return jsonify(results), 200
    else:
        return jsonify({'message': 'Student not found'}), 404

# 3.  add a new progress report
@app.route('/api/progress_report', methods=['POST'])
def add_progress_report():
    data = request.get_json()
    connection = get_db_connection(app)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO progress_reports (student_id, subject, score, feedback, report_date) VALUES (%s, %s, %s, %s, %s)",
        (data['student_id'], data['subject'], data['score'], data['feedback'], data['report_date']))

    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Progress report added successfully!'}), 201

# main function to run the app
if __name__ == '__main__':
    app.run(debug=True)





