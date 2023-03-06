from ResortApp import app
from ResortApp import mysql
from flask import render_template, redirect
from flask import request
from ResortApp.dbutilities import guest_utilities
from ResortApp.user import role_required


@app.route("/new-user", methods=['GET'])
@role_required(['Admin', 'Manager', 'Guest'])
def new_customer():
    try:
        role = request.cookies.get('role')
        user_name = request.cookies.get('userID')
        try:
            guest_name = request.args['guest_name']
            ID, age, contact_info, email_address = guest_utilities.user_by_name(guest_name)
            # return age, contact_info, email_address
            return render_template('new_userpage.html', ID=ID, guest_name=guest_name, age=age,
                                   contact_info=contact_info, email_address=email_address, operation="update",
                                   title="Update User", user_name=user_name, role=role)
        except:
            return render_template('new_userpage.html', title="New User", user_name=user_name, role=role)

    except:
        try:
            guest_name = request.args['guest_name']
            ID, age, contact_info, email_address = guest_utilities.user_by_name(guest_name)
            # return age, contact_info, email_address
            return render_template('new_userpage.html', ID=ID, guest_name=guest_name, age=age,
                                   contact_info=contact_info, email_address=email_address, operation="update",
                                   title="Update User", user_name="", role="")
        except:
            return render_template('new_userpage.html', title="New User", user_name="", role="")


@app.route("/update-user/<ID>", methods=['POST'])
def update_user(ID):
    guest_name = request.form['guest_name']
    age = request.form['age']
    contact_info = request.form['contact_info']
    email = request.form['email']
    guest_utilities.update_guest(ID, guest_name, age, contact_info, email)
    return redirect('/guests')


@app.route("/new-user", methods=['POST'])
def create_customer():
    guest_name = request.form['guest_name']
    age = request.form['age']
    contact_info = request.form['contact_info']
    email = request.form['email']
    guest_utilities.create_user(guest_name, age, contact_info, email)
    return redirect('/guests')


@app.route('/remove/<guest_name>', methods=['GET'])
def remove(guest_name):
    guest_utilities.delete_user(guest_name)
    return redirect('/guests')


# @app.route('/updateuser', methods=['POST'])
# def update(guest_name):
#     cursor = mysql.connection.cursor()
#     query2 = ""
#     cursor.execute(query2, guest_name)
#     mysql.connection.commit()
#     return redirect("/guests")
