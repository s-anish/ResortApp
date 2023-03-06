from flask import render_template, make_response, redirect, request
from ResortApp import app
from ResortApp.user import role_required
# from ResortApp import mysql
from ResortApp.dbutilities import roomutilities
from ResortApp.dbutilities import guest_utilities


@app.route('/', methods=['GET'])
def main_page():
    try:
        role = request.cookies.get('role')
        user_name = request.cookies.get('userID')
        return render_template('mainpage.html', user_name=user_name, role=role)
    except:
        return render_template('mainpage.html', user_name="", role="")


@app.route('/guests', methods=['GET'])
@role_required(['Admin', 'Manager'])
def users():
    records = guest_utilities.get_user()
    try:
        role = request.cookies.get('role')
        user_name = request.cookies.get('userID')
        return render_template('userpage.html', records=records, user_name=user_name, role=role)
    except:
        return render_template('userpage.html', records=records, user_name="", role="")


@app.route('/rooms', methods=['GET'])
def bookings_list():
    booked_rooms = roomutilities.get_booked_rooms()
    total_rooms = roomutilities.get_total_rooms()
    available_rooms = roomutilities.get_available_rooms()
    available_records = roomutilities.get_rooms()
    booked_records, guest_records = roomutilities.booked_rooms()
    try:
        role = request.cookies.get('role')
        user_name = request.cookies.get('userID')
        return render_template('rooms.html', user_name=user_name, role=role, total_rooms=total_rooms, booked_rooms=booked_rooms, available_rooms=available_rooms, available_records=available_records, booked_records=booked_records, guest_records=guest_records)

    except:
        return render_template('rooms.html', user_name="", role="", total_rooms=total_rooms, booked_rooms=booked_rooms, available_rooms=available_rooms, available_records=available_records, booked_records=booked_records, guest_records=guest_records)


@app.route('/reservation/<room_number>', methods=['GET'])
@role_required(['Admin', 'Manager', 'Guest'])
def book(room_number):
    try:
        role = request.cookies.get('role')
        user_name = request.cookies.get('userID')
        return render_template('bookroom.html', room_number=room_number, user_name=user_name, role=role)
    except:
        return render_template('bookroom.html', room_number=room_number, user_name="", role="")


@app.route('/reservation/<room_number>', methods=['POST'])
@role_required(['Admin', 'Manager', 'Guest'])
def book_room(room_number):
    guest_name = request.form['username']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    no_of_guests = request.form['no_of_guests']
    roomutilities.create_bookings(guest_name, room_number, start_date, end_date, no_of_guests)

    return redirect("/rooms")


@app.route('/cancellation/<room_number>', methods=['GET'])
@role_required(['Admin', 'Manager', 'Guest'])
def cancellation(room_number):
    roomutilities.cancel_bookings(room_number)
    return redirect("/rooms")

