from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import date

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)



@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'role' in request.form:
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s AND role= %s', (username, password,role ))
        user = cursor.fetchone()
        if user:
            if user['role'] == 'admin':
                    session['loggedin'] =True
                    #session['id'] = user['id']
                    session['username'] = user['username']
                    session['password'] = user['password']
                    mesage = 'Logged in successfully !'
                    return redirect(url_for('admin'))


            elif user['role'] == 'andwemedia':
                session['loggedin'] = True
                #session['id'] = user['id']
                session['username'] = user['username']
                session['password'] = user['password']
                mesage = 'Logged in successfully !'
                return redirect(url_for('today',mesage=mesage))

            elif user['role'] == 'viw3d':
                session['loggedin'] = True
                #session['id'] = user['id']
                session['username'] = user['username']
                session['password'] = user['password']
                mesage = 'Logged in successfully !'
                return redirect(url_for('Indexv',mesage=mesage))
            elif user['role'] == 'micrografix':
                session['loggedin'] = True
                # session['id'] = user['id']
                session['username'] = user['username']
                session['password'] = user['password']
                mesage = 'Logged in successfully !'
                return redirect(url_for('Indexm',mesage=mesage))
            else:
               mesage = 'Only admin can login'
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)

@app.route('/')
@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/index')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    iiq=cur.execute("select count(*) from students where status='IN QUE' ")
    iiq=cur.fetchone()[0]
    v=cur.execute("select count(*) from students where  d=curdate()  ")
    v=cur.fetchone()[0]
    com=cur.execute("select count(*) from students where status='completed' ")
    com=cur.fetchone()[0]
    cur.close()

    return render_template('index2.html',students=data,com=com,tod=v,iiq=iiq)

@app.route('/viwindex')
def Indexviw():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM viw3d")
    data = cur.fetchall()
    iiq=cur.execute("select count(*) from viw3d where status='IN QUE' ")
    iiq=cur.fetchone()[0]
    v=cur.execute("select count(*) from viw3d where  date_v=curdate()  ")
    v=cur.fetchone()[0]
    com=cur.execute("select count(*) from viw3d where status='completed' ")
    com=cur.fetchone()[0]
    cur.close()

    return render_template('index3.html',viw3d=data,com=com,tod=v,iiq=iiq)


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        status= request.form['status']
        priority = request.form['priority']
        d= request.form['d']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name,email, phone,status,priority,d) VALUES (%s, %s, %s,%s,%s,%s)", (name,email, phone,status,priority,d))
        mysql.connection.commit()
        return redirect(url_for('Index'))

# ========================================viw3d insert===================================================
@app.route('/vinsert', methods = ['POST'])
def vinsert():

    if request.method == "POST":
       
        flash("Data Inserted Successfully")
        name = request.form['name']
        task = request.form['task']
        assign = request.form['assign']
        status= request.form['status']
        priority = request.form['priority']
        date_v= request.form['date_v']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO viw3d (name, task, assign,status,priority,date_v) VALUES (%s, %s, %s,%s,%s,%s)", (name, task, assign,status,priority,date_v))
        mysql.connection.commit()
        return redirect(url_for('Indexviw',viw3d=date_v))

@app.route('/admin')
def admin():
    if 'loggedin'  in session:
        curr=mysql.connection.cursor()
        curr.execute('SELECT * from students where d=curdate()')
        f=curr.fetchall()
        # curr.execute('SELECT * from micrografix where d=curdate()')
        # m=curr.fetchall()
        # curr.execute('SELECT * from viw3d where d=curdate()')
        # v=curr.fetchall()
        curr.close()
        return render_template("admin.html",students=f)
    return redirect(url_for('login'))





@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/done/<string:id_data>/', methods = ['POST','GET'])
def done(id_data):
   
        cur=mysql.connection.cursor()
        cur.execute("UPDATE students set status='COMPLETED'  where id=%s ",(id_data,))
        mysql.connection.commit()
        return redirect(url_for('today'))

@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        # name=request.form.get('cname')
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        status= request.form['status']
        priority = request.form['priority']
        d= request.form['d']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s,status=%s,priority=%s,d=%s
               WHERE id=%s
            """, (name, email, phone,status,priority,d, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

# =============================viw3d update task================================================
@app.route('/vupdate',methods=['POST','GET'])
def vupdate():

    if request.method == 'POST':
        # name=request.form.get('cname')
        id_data = request.form['id']
        name = request.form['name']
        task = request.form['task']
        assign = request.form['assign']
        status= request.form['status']
        priority = request.form['priority']
        date_v= request.form['date_v']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE viw3d
               SET name=%s, task = %s, assign=%s,status=%s,priority=%s,date_v=%s
               WHERE id=%s
            """, (name,task,assign,status,priority,date_v, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Indexviw'))

@app.route('/today',methods=['POST','GET'])
def today():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students where d=curdate() and (status='in que' or status='completed' or status='todays task') ")
    data = cur.fetchall()
    cur.execute("UPDATE students set status='TODAYS TASK'  where status='in que'  AND d=curdate() ")
    
    iiq=cur.execute("select count(*) from students where status='in que' ")
    iiq=cur.fetchone()[0]
    v=cur.execute("select count(*) from students where  d=curdate()  ")
    v=cur.fetchone()[0]
    com=cur.execute("select count(*) from students where status='completed' ")
    com=cur.fetchone()[0]
    cur.close()

    return render_template('index2.html', students=data,com=com,tod=v,iiq=iiq )
    
@app.route('/inque',methods=['POST','GET'])
def inque():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students where status='in que' ")
    data = cur.fetchall()
    com=cur.execute("select count(*) from students where status='completed' ")
    com=cur.fetchone()[0]
    iiq=cur.execute("select count(*) from students where status='IN QUE' ")
    iiq=cur.fetchone()[0]
    v=cur.execute("select count(*) from students where  d=curdate() ")
    v=cur.fetchone()[0]
    cur.close()

    return render_template('index2.html', students=data,com=com,tod=v,iiq=iiq )

@app.route('/completed1',methods=['POST','GET'])
def completed1():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students where status='completed' ")
    data = cur.fetchall()
    com=cur.execute("select count(*) from students where status='completed' ")
    com=cur.fetchone()[0]
    v=cur.execute("select count(*) from students where  d=curdate() ")
    v=cur.fetchone()[0]
    iiq=cur.execute("select count(*) from students where status='IN QUE' ")
    iiq=cur.fetchone()[0]
    

    cur.close()

    return render_template('index2.html', students=data,com=com,tod=v,iiq=iiq )

@app.route('/t', methods = ['GET', 'POST'])
def t():
 d=""
 if request.method=='POST':
    dt=request.form['d']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM students where d LIKE %s",(dt,))
    d=cur.fetchall()
    com=cur.execute("select count(*) from students where status='COMPLETED' ")
    com=cur.fetchone()[0]
    iiq=cur.execute("select count(*) from students where status='IN QUE' ")
    iiq=cur.fetchone()[0]
    v=cur.execute("select count(*) from students where  d=curdate() ")
    v=cur.fetchone()[0]
    cur.close()
 return render_template("index2.html",students=d,com=com,tod=v,iiq=iiq)

#  ======================================for viw3d=========================
@app.route('/vt', methods = ['GET', 'POST'])
def vt():
 d=""
 if request.method=='POST':
    dt=request.form['date_v']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM viw3d where date_v LIKE %s",(dt,))
    d=cur.fetchall()
    com=cur.execute("select count(*) from viw3d where status='COMPLETED' ")
    com=cur.fetchone()[0]
    iiq=cur.execute("select count(*) from viw3d where status='IN QUE' ")
    iiq=cur.fetchone()[0]
    v=cur.execute("select count(*) from viw3d where  date_v=curdate() ")
    v=cur.fetchone()[0]
    cur.close()
 return render_template("index3.html",viw3d=d,com=com,tod=v,iiq=iiq)

# CLient table for andwemedia+====================================================================================================================

@app.route('/clientandwemedia')
def clienttableandwemedia():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM clienttable;")
    data = cur.fetchall()
    cur.close()
    return render_template('clienttable.html',clienttable=data,)

@app.route('/insertclient', methods = ['POST'])
def insertclient():

    if request.method == "POST":
        flash("Data Inserted Successfully")
       
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        project = request.form['project']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clienttable (name, email, phone,project) VALUES (%s, %s, %s,%s)", (name, email, phone,project))
        mysql.connection.commit()
        return redirect(url_for('clienttableandwemedia'))

@app.route('/updateclient',methods=['POST','GET'])
def updateclient():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        project= request.form['project']
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE clienttable
               SET name=%s, email=%s, phone=%s,project=%s
               WHERE id=%s
            """, (name, email, phone,project,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('clienttableandwemedia'))

@app.route('/deleteclient/<string:id_data>', methods = ['GET'])
def deleteclient(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM clienttable WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('clienttableandwemedia'))

@app.route('/totalclient')
def totalclient():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM clienttable")
    data = cur.fetchall()
  
    cur.close()

    return render_template('clienttable.html', clienttable=data)

if __name__ == "__main__":
    app.run(debug=True)
