-- SQL file for API assignment 
-- Creating data on student progress for key stage 1 (year 1 & 2)

CREATE DATABASE student_progress_db;

CREATE TABLE students (
id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
year_group VARCHAR(10),
teacher VARCHAR(70)
);

CREATE TABLE progress_reports (
id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
subject VARCHAR(50),
score FLOAT,
feedback TEXT,
report_date DATE,
FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Test data for testing purposes 
-- Data for students 
INSERT INTO students (first_name, last_name, year_group, teacher) VALUES
('Joshua', 'Reid', 'yr_1', 'Mrs_Lamani'),
('Aleena', 'Rahman', 'yr_1', 'Mrs_Lamani'),
('Lucas', 'Thompson', 'yr_1', 'Mrs_Lamani'),
('Bianca', 'Alheri', 'yr_1', 'Mrs_Lamani'),
('Zeena', 'Williams', 'yr_1', 'Mrs_Lamani'),
('Clark', 'Benson', 'yr_2', 'Mr_Oats'),
('Terelle', 'Addo', 'yr_2', 'Mr_Oats'),
('Yasmine', 'Mensah', 'yr_2', 'Mr_Oats'),
('Steven', 'Anderson', 'yr_2', 'Mr_Oast'),
('Mashonda', 'Kanneh', 'yr_2', 'Mr_Oats');

-- Data for progress reports
INSERT INTO progress_reports (student_id, subject, score, feedback, report_date) VALUES
('1', 'Maths', 74.0, 'Working above target', '2024-07-13'),
('1', 'English', 70.0, 'Working above target', '2024-07-13'),
('1', 'Science', 75.0, 'Working above target', '2024-07-13'),
('2', 'Maths', 50.0, 'Working below target', '2024-07-13'),
('2', 'English', 79.0, 'Working above target', '2024-07-13'),
('2', 'Science', 69.0, 'Working above target', '2024-07-13'),
('3', 'Maths', 49.0, 'Working on target', '2024-07-13'),
('3', 'English', 60.0, 'Working on target', '2024-07-13'),
('3', 'Science', 70.0, 'Working on target', '2024-07-13'),
('4', 'Maths', 38.0, 'Working below target', '2024-07-13'),
('4', 'English', 45.0, 'Working on target', '2024-07-13'),
('4', 'Science', 77.0, 'Working above target', '2024-07-13'),
('5', 'Maths', 68.0, 'Working on target', '2024-07-13'),
('5', 'English', 75.0, 'Working on target', '2024-07-13'),
('5', 'Science', 80.0, 'Working on target', '2024-07-13'),
('6', 'Maths', 28.0, 'Working below target', '2024-07-17'),
('6', 'English', 53.0, 'Working above target', '2024-07-17'),
('6', 'Science', 68.0, 'Working on target', '2024-07-17'),
('7', 'Maths', 92.0, 'Working above target', '2024-07-17'),
('7', 'English', 78.0, 'Working above target', '2024-07-17'),
('7', 'Science', 62.0, 'Working at target', '2024-07-17'),
('8', 'Maths', 18.0, 'Working below target', '2024-07-17'),
('8', 'English', 50.0, 'Working at target', '2024-07-17'),
('8', 'Science', 51.0, 'Working at target', '2024-07-17'),
('9', 'Maths', 23.0, 'Working at target', '2024-07-17'),
('9', 'English', 45.0, 'Working at target', '2024-07-17'),
('9', 'Science', 38.0, 'Working at target', '2024-07-17'),
('10', 'Maths', 70.0, 'Working at target', '2024-07-17'),
('10', 'English', 80.0, 'Working at target', '2024-07-17'),
('10', 'Science', 89.0, 'Working at target', '2024-07-17');

-- Queries that my API will use to interact with the database

-- This query will count students working towards their target 
SELECT COUNT(*) AS num_students_working_on_target
FROM progress_reports
WHERE feedback = 'Working on target';

-- This query is to find out how many year 1 students are working above target with the subject listed. 
-- I am going to join the students and progress_reports tables and filter by year 1 and working above target feedback.
SELECT s.first_name, s.last_name, p.subject, p.score, p.feedback, p.report_date
FROM students s
JOIN progress_reports p ON s.id = p.student_id
WHERE s.id = student_id;

-- This query is to retrive progress for a specific student
-- You should beable to replace student id by putting in the specific id number
SELECT s.first_name, s.last_name, p.subject, p.score, p.feedback, p.report_date
FROM students s
JOIN progress_reports p ON s.id = p.student_id
WHERE s.id = student_id;







