from flask import Flask, request, redirect, render_template
from functions.sqlquery import sql_query, sql_query2, sql_edit_insert, sql_delete

app = Flask(__name__)

@app.route('/')
def sql_database():
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'SELECT * FROM data_table'
    return render_template('index.html', results=results, msg=msg)

@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        sql_edit_insert(''' INSERT INTO data_table (first_name,last_name,address,city,state,zip) VALUES (?,?,?,?,?,?) ''', (first_name,last_name,address,city,state,zip) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'INSERT INTO data_table (first_name,last_name,address,city,state,zip) VALUES ('+first_name+','+last_name+','+address+','+city+','+state+','+zip+')'
    return render_template('index.html', results=results, msg=msg)

@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM data_table where first_name = ? and last_name = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'DELETE FROM data_table WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('index.html', results=results, msg=msg)

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    if request.method == 'GET':
        elname = request.args.get('elname')
        efname = request.args.get('efname')
        eresults = sql_query2(''' SELECT * FROM data_table where first_name = ? and last_name = ?''', (efname,elname))
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('index.html', eresults=eresults, results=results)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    if request.method == 'POST':
        old_last_name = request.form['old_last_name']
        old_first_name = request.form['old_first_name']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        sql_edit_insert(''' UPDATE data_table set first_name=?,last_name=?,address=?,city=?,state=?,zip=? WHERE first_name=? and last_name=? ''', (first_name,last_name,address,city,state,zip,old_first_name,old_last_name) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'UPDATE data_table set first_name = ' + first_name + ', last_name = ' + last_name + ', address = ' + address + ', city = ' + city + ', state = ' + state + ', zip = ' + zip + ' WHERE first_name = ' + old_first_name + ' and last_name = ' + old_last_name
    return render_template('index.html', results=results, msg=msg)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
