from ResortApp import app
from ResortApp import mysql


def get_booked_rooms():
    cursor = mysql.connection.cursor()
    query2 = 'SELECT Count(ID) FROM bookings'
    cursor.execute(query2)
    booked_rooms = cursor.fetchall()
    booked_rooms = booked_rooms[0]
    booked_rooms = booked_rooms[0]

    return booked_rooms


def get_total_rooms():
    cursor = mysql.connection.cursor()
    query1 = "SELECT Count(ID) FROM rooms"
    cursor.execute(query1)
    total_rooms = cursor.fetchall()
    total_rooms = total_rooms[0]
    total_rooms = total_rooms[0]
    return total_rooms


def get_available_rooms():
    total_rooms = get_total_rooms()
    booked_rooms = get_booked_rooms()
    available_rooms = total_rooms - booked_rooms
    return available_rooms


def get_rooms():
    cursor = mysql.connection.cursor()
    query = 'SELECT rooms.room_number, rooms.price, rooms.capacity FROM rooms'
    query += ' LEFT JOIN bookings ON bookings.room_id=rooms.id WHERE bookings.room_id is null'
    cursor.execute(query)
    available_records = cursor.fetchall()
    return available_records


def booked_rooms():
    cursor = mysql.connection.cursor()
    query1 = 'SELECT rooms.room_number, rooms.price, bookings.no_of_people FROM rooms'
    query1 += ' LEFT JOIN bookings ON bookings.room_id=rooms.id WHERE bookings.room_id is not null'
    cursor.execute(query1)
    booked_records = cursor.fetchall()

    query2 = "SELECT guests.guest_name FROM guests LEFT JOIN bookings"
    query2 += " ON bookings.guest_id=guests.ID WHERE bookings.guest_id is not null"
    cursor.execute(query2)
    guest_records = cursor.fetchall()
    return booked_records, guest_records


def create_bookings(guest_name, room_number, start_date, end_date, no_of_guests):
    cursor = mysql.connection.cursor()
    query1 = 'SELECT ID FROM guests WHERE guest_name=%s'
    cursor.execute(query1, [guest_name])
    guest_id = cursor.fetchall()
    guest_id = guest_id[0]
    guest_id = guest_id[0]

    query2 = 'SELECT ID FROM rooms WHERE room_number=%s'
    cursor.execute(query2, [room_number])
    room_id = cursor.fetchall()
    room_id = room_id[0]
    room_id = room_id[0]

    query2 = 'INSERT INTO bookings (guest_id, room_id, no_of_people, start_date, end_date) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(query2, [guest_id, room_id, no_of_guests, start_date, end_date])
    mysql.connection.commit()


def cancel_bookings(room_number):
    cursor = mysql.connection.cursor()

    query2 = 'SELECT ID FROM rooms WHERE room_number=%s'
    cursor.execute(query2, [room_number])
    room_id = cursor.fetchall()
    room_id = room_id[0]
    room_id = room_id[0]

    max_number = 1000
    min_number = 100
    query2 = "DELETE FROM bookings WHERE room_id=%s"
    cursor.execute(query2, [room_id])
    mysql.connection.commit()
