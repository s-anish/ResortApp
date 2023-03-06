from flask import request
from ResortApp import mysql


def create_user(guest_name, age, contact_info, email):
    cursor = mysql.connection.cursor()
    query = "INSERT INTO guests (guest_name, age, contact_info, email_address) values (%s, %s, %s, %s)"
    cursor.execute(query, [guest_name, age, contact_info, email])
    mysql.connection.commit()


def get_user():
    cursor = mysql.connection.cursor()
    query = "SELECT guest_name, age, contact_info, email_address FROM guests"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def user_by_name(guest_name):
    cursor = mysql.connection.cursor()
    query = "SELECT ID, age, contact_info, email_address FROM guests WHERE guest_name=%s"
    cursor.execute(query, [guest_name])
    records = cursor.fetchall()
    ID = records[0]
    ID = ID[0]

    age = records[0]
    age = age[1]

    contact_info = records[0]
    contact_info = contact_info[2]

    email_address = records[0]
    email_address = email_address[3]
    return ID, age, contact_info, email_address


def delete_user(guest_name):
    query1 = "SELECT ID FROM guests WHERE guest_name=%s"
    cursor = mysql.connection.cursor()
    cursor.execute(query1, [guest_name])
    guest_id = cursor.fetchall()
    guest_id = guest_id[0]
    guest_id = guest_id[0]

    query2 = "DELETE FROM guests WHERE ID=%s"
    cursor.execute(query2, [guest_id])
    mysql.connection.commit()


def update_guest(ID, guest_name, age, contact_info, email_address):
    cursor = mysql.connection.cursor()
    query = "UPDATE guests SET guest_name=%s, age=%s, contact_info=%s, email_address=%s WHERE ID=%s"
    cursor.execute(query, [guest_name, age, contact_info, email_address, ID])
    mysql.connection.commit()


def get_role(user, email, password):
    cursor = mysql.connection.cursor()
    query = "SELECT assigned_role FROM users WHERE name=%s and email=%s and password=%s"
    cursor.execute(query, [user, email, password])
    records = cursor.fetchall()
    try:
        role = records[0]
        role = role[0]
        message = "Success"
    except:
        role = None
        message = "No such Person exist"
    return role, message
