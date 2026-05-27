from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-this-in-production'

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
        
        # Print to console (in production, you'd send an email)
        print(f"📧 New Contact Message:")
        print(f"   Name: {name}")
        print(f"   Email: {email}")
        print(f"   Message: {message}")
        print("-" * 50)
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)