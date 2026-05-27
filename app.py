import os
from flask import Flask, render_template, request, redirect, url_for

# Get the absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
           template_folder=os.path.join(basedir, 'Templates'),
           static_folder=os.path.join(basedir, 'Static'))
app.secret_key = 'your-secret-key-change-this-for-production'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"📧 New Contact Message:")
        print(f"   Name: {name}")
        print(f"   Email: {email}")
        print(f"   Message: {message}")
        print("-" * 50)
        
        return '', 204
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
