from flask import Flask, render_template, request, redirect, url_for, flash
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a more secure key

# Connect to MySQL database


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='CloudPital Home')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

@app.route('/hosp_login.html', methods=['POST', 'GET'])
def hosp_login():
    if request.method == 'POST':
        id = request.form['ID']
        password = request.form['password']

        cursor = conn.cursor()

        # Check if the hospital with the provided ID and password exists
        cursor.execute('SELECT * FROM hospital WHERE id=%s AND password=%s', (id, password))
        hospital = cursor.fetchone()

        cursor.close()

        if hospital:
            return "Form submitted successfully" 
            return redirect(url_for('hosp_dashboard'))
        else:
            flash('Wrong credentials. Please try again.', 'danger')

    return render_template('hosp_login.html', the_title='Hospital Login')


@app.route('/hosp_dashboard.html')
def hosp_dashboard():
    return render_template('hosp_dashboard.html', the_title='Hospital Dashboard')

if __name__ == '__main__':
    app.run(debug=True)
