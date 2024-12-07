from flask import Flask, request, render_template
from counselling import *
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jossa')
def jossa():
    return render_template('form.html', counselling_type='JoSAA')

@app.route('/uptac')
def uptac():
    return render_template('form.html', counselling_type='UPTAC')

@app.route('/csab')
def csab():
    return render_template('form.html', counselling_type='CSAB')

@app.route('/submit', methods=['POST'])
def submit():
    counselling_type = request.form['counsellingType']
    rank = request.form['rank']
    gender = request.form['gender']
    category = request.form['category']
    data=counselling_info(counselling_type,rank,category,gender)
    # Sample data for demonstration purposes
#     data = [{'Institue': 'Indian Institute  of Technology Hyderabad', 'Branch': 'Artificial Intelligence (4 Years, Bachelor of Technology)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '685', 'Closing': '875', 'Chances': 'Low'}, {'Institue': 'Indian Institute  of Technology Kharagpur', 'Branch': 'Artificial Intelligence (4 Years, Bachelor of Technology)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '467', 'Closing': '898', 'Chances': 'Low'}, {'Institue': 'Malaviya National Institute of Technology Jaipur', 'Branch': 'Architecture  (5 Years, Bachelor of Architecture)', 'Quota': 'OS', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '497', 'Closing': '926', 'Chances': 'Low'}, {'Institue': 'Indian Institute  of Technology Bombay', 'Branch': 'Electrical Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '536', 'Closing': '973', 'Chances': 'Low'}, {'Institue': 'Indian Institute  of Technology Hyderabad', 'Branch': 'Mathematics and Computing (4 Years, Bachelor of Technology)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '660', 'Closing': '982', 'Chances': 'Low'}, {'Institue': 'Indian Institute  of Technology Kanpur', 'Branch': 'Mathematics and Scientific Computing (4 Years, Bachelor of Science)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '756', 'Closing': '990', 'Chances': 'Low'}, {'Institue': 'Indian Institute  of Technology Guwahati', 'Branch': 'Data Science and Artificial Intelligence (4 Years, Bachelor of Technology)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '829', 'Closing': '995', 'Chances': 'Low'}, {'Institue': 'Visvesvaraya National Institute of Technology, Nagpur', 'Branch': 
# 'Architecture  (5 Years, Bachelor of Architecture)', 'Quota': 'OS', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '537', 'Closing': '1002', 'Chances': 'Moderate'}, {'Institue': 'Indian Institute  of Technology Guwahati', 'Branch': 'Mathematics and Computing (4 Years, Bachelor of Technology)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '722', 'Closing': '1021', 'Chances': 'Moderate'}, {'Institue': 'Indian Institute  of Technology Kanpur', 'Branch': 'Statistics and Data Science (4 Years, Bachelor of Science)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '699', 'Closing': '1030', 'Chances': 'Moderate'}, {'Institue': 'School of Planning & Architecture: Vijayawada', 'Branch': 'Planning (4 Years, Bachelor of Planning)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '226', 'Closing': '1039', 'Chances': 'Moderate'}, {'Institue': 'Indian Institute  of Technology (BHU) Varanasi', 'Branch': 'Computer Science and Engineering (4 Years, Bachelor of Technology)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '667', 'Closing': '1071', 'Chances': 'Moderate'}, {'Institue': 'School of Planning & Architecture, Bhopal', 'Branch': 'Planning (4 Years, Bachelor of Planning)', 'Quota': 'AI', 'Category': 'OPEN', 'Gender': 'Neutral', 'Opening': '109', 'Closing': '1093', 'Chances': 'High'}]
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run()
