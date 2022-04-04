from flask import Blueprint, render_template, request
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

select = Blueprint('select', __name__)

@select.route('/employee')
def sEmployee():

    cur = conn.cursor()
    try:
        insertQuery = "select * from person;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sEmployee.html', rows = rows)

@select.route('/employee/search', methods = ['GET', 'POST'])
def sEmployeeSearch():
    pattern = request.form.get('pattern')
    
    cur = conn.cursor()

    try:
        insertQuery = "select * from person where name like '%" + pattern + "%' or surname like '%" + pattern + "%';"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()

    return render_template('select/sEmployee.html', rows = rows)

@select.route('/clients')
def sClient():

    cur = conn.cursor()
    try:
        insertQuery = "select * from client;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sClient.html', rows = rows)

@select.route('/equipment')
def sEquipment():

    cur = conn.cursor()
    try:
        insertQuery = "select * from equipment;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sEquipment.html', rows = rows)

@select.route('/sowing')
def sSowing():

    cur = conn.cursor()
    try:
        insertQuery = "select * from sowing;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sSowing.html', rows = rows)

@select.route('/harvest')
def sHarvest():
    cur = conn.cursor()

    try:
        insertQuery = "select * from harvest;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sHarvest.html', rows = rows)

@select.route('/weeding')
def sWeeding():
    cur = conn.cursor()

    try:
        insertQuery = "select * from weeding;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sWeeding.html', rows = rows)

@select.route('/transaction')
def sTransactions():
    cur = conn.cursor()

    try:
        insertQuery = "select * from transaction;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sTransaction.html', rows = rows)

@select.route('/lodging')
def sLodging():
    cur = conn.cursor()

    try:
        insertQuery = "select * from lodging;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sLodging.html', rows = rows)

@select.route('/farmland')
def sFarmland():
    cur = conn.cursor()

    try:
        insertQuery = "select * from farmland;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    
    return render_template('select/sFarmland.html', rows = rows)

@select.route('/warehouse')
def sWarehouse():
    cur = conn.cursor()
    try:
        insertQuery = "select * from warehouse;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sWarehouse.html',rows = rows)