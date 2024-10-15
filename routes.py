#routes.py
from flask import Blueprint, jsonify
from .db_utils import get_db_connection, close_db_connection

api = Blueprint('api', '_name_')
@api.route('/students/working-on-target', mathods=['GET'])
def get_students_working_on_target():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute()
