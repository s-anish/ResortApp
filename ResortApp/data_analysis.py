from ResortApp import sqlEngine, app
from flask import render_template, Response
import matplotlib.pyplot as plt
from sqlalchemy import text
import pandas as pd
import io

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

dbConnection = sqlEngine.connect()

room_details = pd.read_sql(text("select * from room_details "), dbConnection)
weekly_bookings_single = pd.read_sql(text("select * from weekly_bookings where details_ID = 1"), dbConnection)
weekly_bookings_double = pd.read_sql(text("select * from weekly_bookings where details_ID = 2"), dbConnection)
weekly_bookings_special = pd.read_sql(text("select * from weekly_bookings where details_ID = 3"), dbConnection)
weekly_bookings_sea_view = pd.read_sql(text("select * from weekly_bookings where details_ID = 4"), dbConnection)

pd.set_option('display.expand_frame_repr', False)

dbConnection.close()
# plt.show()


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/weekly-stats')
def stats():
    x = weekly_bookings_single['week_number']
    y = weekly_bookings_single['booked_rooms']
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(12, 4))
    ax1.plot(x, y)
    ax1.set_xlabel('occupancy in X month')
    ax1.set_ylabel('number of rooms booked')
    ax1.set_title('occupancy of single bed rooms')

    x = weekly_bookings_double['week_number']
    y = weekly_bookings_double['booked_rooms']
    ax2.plot(x, y)
    ax2.set_xlabel('occupancy in X month')
    ax2.set_ylabel('number of rooms booked')
    ax2.set_title('occupancy of double bed rooms')

    x = weekly_bookings_special['week_number']
    y = weekly_bookings_special['booked_rooms']
    ax3.plot(x, y)
    ax3.set_xlabel('occupancy in X month')
    ax3.set_ylabel('number of rooms booked')
    ax3.set_title('occupancy of special rooms')

    x = weekly_bookings_sea_view['week_number']
    y = weekly_bookings_sea_view['booked_rooms']
    ax4.plot(x, y)
    ax4.set_xlabel('occupancy in X month')
    ax4.set_ylabel('number of rooms booked')
    ax4.set_title('occupancy of sea view rooms')
    plt.tight_layout()
    # Save the plot to a PNG image in memory.
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    # Return the PNG image as a Flask response.
    return Response(img.getvalue(), mimetype='image/png')
