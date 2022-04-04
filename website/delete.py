from flask import Blueprint, render_template, request, flash, jsonify
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

delete = Blueprint('delete', __name__)

@delete.route('/employee', methods = ['GET', 'POST'])
def dEmployee():
    if request.method == 'POST':
        pesel = request.form.get('pesel')
        
        cur = conn.cursor()
        
        try:
            insertQuery = "select * from person where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct pesel", category = 'error')
                return render_template('delete/dEmployee.html')

            insertQuery = "delete from person where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            conn.commit()

            print("Employee deleted")
            flash("Employee deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('delete/dEmployee.html')

@delete.route('/client', methods = ['GET', 'POST'])
def dClient():
    if request.method == 'POST':
        pesel = request.form.get('pesel')

        cur = conn.cursor()
        
        try:
            insertQuery = "select * from client where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct pesel", category = 'error')
                return render_template('delete/dClient.html')

            insertQuery = "delete from client where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            conn.commit()

            print("Client deleted")
            flash("Client deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('delete/dClient.html')

@delete.route('/equipment', methods = ['GET', 'POST'])
def dEquipment():
    if request.method == 'POST':
        id = request.form.get('id')

        cur = conn.cursor()

        try:
            insertQuery = "select * from equipment where id = %s;"
            cur.execute(insertQuery, (id,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct id", category = 'error')
                return render_template('delete/dEquipment.html')

            insertQuery = "delete from equipment where id = %s;"
            cur.execute(insertQuery, (id,))
            conn.commit()

            print("Equipment deleted")
            flash("Equipment deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('delete/dEquipment.html')

@delete.route('/farmland', methods = ['GET', 'POST'])
def dFarmland():
    if request.method == 'POST':
        address = request.form.get('address')

        cur = conn.cursor()

        try:
            insertQuery = "select * from farmland where address = %s;"
            cur.execute(insertQuery, (address,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct address", category = 'error')
                return render_template('delete/dFarmland.html')

            insertQuery = "delete from farmland where address = %s;"
            cur.execute(insertQuery, (address,))
            conn.commit()

            print("Farmland deleted")
            flash("Farmland deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('delete/dFarmland.html')

@delete.route('/lodging', methods = ['GET', 'POST'])
def dLodging():
    if request.method == 'POST':
        address = request.form.get('address')

        cur = conn.cursor()
        
        try:
            insertQuery = "select * from lodging where address = %s;"
            cur.execute(insertQuery, (address,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct address", category = 'error')
                return render_template('delete/dLodging.html')

            insertQuery = "delete from lodging where address = %s;"
            cur.execute(insertQuery, (address,))
            conn.commit()

            print("Lodging deleted")
            flash("Lodging deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('delete/dLodging.html')

@delete.route('/warehouse', methods = ['GET', 'POST'])
def dWarehouse():
    if request.method == 'POST':
        address = request.form.get('address')

        cur = conn.cursor()
        
        try:
            insertQuery = "select * from warehouse where address = %s;"
            cur.execute(insertQuery, (address,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct address", category = 'error')
                return render_template('delete/dWarehouse.html')

            insertQuery = "delete from warehouse where address = %s;"
            cur.execute(insertQuery, (address,))
            conn.commit()

            print("Warehouse deleted")
            flash("Warehouse deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dWarehouse.html')

@delete.route('/sowing', methods = ['GET', 'POST'])
def iSowing():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')

        cur = conn.cursor()
        
        try:
            insertQuery = "select * from sowing where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct date", category = 'error')
                return render_template('delete/dSowing.html')

            insertQuery = "delete from sowing where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            conn.commit()

            print("Sowing deleted")
            flash("Sowing deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dSowing.html')

@delete.route('/harvest', methods = ['GET', 'POST'])
def iHarvest():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')

        cur = conn.cursor()
        
        try:
            insertQuery = "select * from harvest where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct date", category = 'error')
                return render_template('delete/dHarvest.html')

            insertQuery = "delete from harvest where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            conn.commit()

            print("Harvest deleted")
            flash("Harvest deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dHarvest.html')

@delete.route('/weeding', methods = ['GET', 'POST'])
def iWeeding():

    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')

        cur = conn.cursor()
        
        try:
            insertQuery = "select * from weeding where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct date", category = 'error')
                return render_template('delete/dWeeding.html')

            insertQuery = "delete from weeding where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            conn.commit()

            print("Weeding deleted")
            flash("Weeding deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dWeeding.html')

@delete.route('/transaction', methods = ['GET', 'POST'])
def dTransaction():

    if request.method == 'POST':
        id = request.form.get('id')

        cur = conn.cursor()
        try:
            insertQuery = "select * from transaction where id = %s;"
            cur.execute(insertQuery, (id,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct id", category = 'error')
                return render_template('delete/dTransaction.html')

            insertQuery = "delete from transaction where id = %s;"
            cur.execute(insertQuery, (id,))
            conn.commit()

            print("Transaction deleted")
            flash("Transaction deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dTransaction.html')