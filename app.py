from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"📧 New message from {name} ({email}): {message}")
        print("-" * 50)
        
        flash('Thank you for your message! I will respond soon.', 'success')
        return redirect(url_for('home') + '#contact')
    
    return render_template('index.html')

@app.route('/download-resume')
def download_resume():
    return send_from_directory('static', 'Akshay_Soni_Resume.docx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)