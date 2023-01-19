from flask import Flask, render_template, request, redirect,flash,jsonify,url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM users")
    userDetails= cur.fetchall()
    cur.close()
    return render_template('users.html', userDetails=userDetails )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['GET','POST'])
def delete(id):
    #flash("Record Has Been Deleted Successfully")
    userDetails = request.form
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('Index'))


@app.route('/update/<string:id>',methods=['POST','GET'])
def update(id):
    if request.method == 'GET':
    	cur = mysql.connection.cursor()
    	cur.execute("SELECT  * FROM users")
    	userDetails=cur.fetchall()
    	cur.execute("SELECT  * FROM users WHERE id=%s",(id,))
    	specificUser=cur.fetchall()
    	cur.close()
    	return render_template('users.html',userDetails=userDetails,flag=True,specificUser=specificUser[0])
    	#cur = mysql.connection.cursor()
    	#resultValue = cur.execute("SELECT * FROM users WHERE id=%s",(id))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET name=%s, email=%s WHERE id=%s ", (name, email, id,))
        mysql.connection.commit()
        #return render_template('user.html', userDetails = userDetails)
        return redirect(url_for('Index'))	



@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(debug=True)
