@app.route('/hosp_dashboard.html')
def hosp_dashboard():
    return render_template('hosp_dashboard.html', the_title='Hospital Dashboard')