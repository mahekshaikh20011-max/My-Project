from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# --- Email Configuration (Lifeline HMS Settings) ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lifelinehms8@gmail.com'
# Aapka 16-digit App Password yahan paste kar diya hai
app.config['MAIL_PASSWORD'] = 'gdkjdveleooefers' 
app.config['MAIL_DEFAULT_SENDER'] = 'lifelinehms8@gmail.com'

mail = Mail(app)

# --- Routes ---

@app.route('/')
def home():
    # Ye aapki index file load karega
    return render_template('index.html')

@app.route('/appointment')
def appointment_page():
    # Ye aapki appointment.html file load karega
    return render_template('appointment.html')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    if request.method == 'POST':
        # Form se details nikalna
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        dept = request.form.get('department')
        date = request.form.get('date')
        user_msg = request.form.get('message')

        # Hospital ko bheja jane wala Email
        subject = f"New Appointment Request: {name}"
        body_content = f"""
        Hello Lifeline HMS Team,
        
        Ek naya appointment request aayi hai:
        
        Patient Name: {name}
        Email: {email}
        Phone: {phone}
        Department: {dept}
        Preferred Date: {date}
        Message: {user_msg}
        
        Regards,
        Lifeline HMS Website System
        """

        msg = Message(subject=subject,
                      recipients=['lifelinehms8@gmail.com'],
                      body=body_content)

        try:
            mail.send(msg)
            return "<h1>Success! Appointment details sent to lifelinehms8@gmail.com. We will contact you soon.</h1>"
        except Exception as e:
            return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
