from flask import Blueprint, render_template, request, flash
from datetime import date, datetime
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

insert = Blueprint('insert', __name__)

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

@insert.route('/employee', methods = ['GET', 'POST'])
def iEmployee():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        pesel = request.form.get('pesel')
        phone = request.form.get('phone')
        birthDate = request.form.get('birthDate')
        salary = request.form.get('salary')
        role = request.form.get('role')
        lodgingAddress = request.form.get('lodgingAddress')
        
        today = date.today()
        birthDate = datetime.strptime(birthDate, '%Y-%m-%d')
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.day, birthDate.day))
    
        if age < 16:
            print("You are too young to work")
            flash("You are too young to work", category = 'error')
        elif any(i.isdigit() for i in name):
            print("Your name cannot conatin digits")
            flash("Your name cannot conatin digits", category = 'error')
        elif any(i.isdigit() for i in surname):
            print("Your surname cannot conatin digits")
            flash("Your surname cannot conatin digits", category = 'error')
        elif float(salary) < 50:
            print("An employee cannot have such a low salary")
            flash("An employee cannot have such a low salary", category = 'error')
    
        cur = conn.cursor()

        try:
            insertQuery = "select currentFreeApartments(%s);"
            cur.execute(insertQuery, (lodgingAddress,))

            if cur.fetchone()[0] <= 0:
                # print("There are no vacancies at this address")
                # flash("There are no vacancies at this address", category = 'error')
                raise Exception("There are no vacancies at this address")

            insertQuery = "insert into person (pesel, name, surname, phone_number, birth_date, salary, role, lodging_address) values (%s, %s, %s, %s, %s, %s, %s, %s);"
            record = (pesel, name, surname, phone, birthDate, salary, role, lodgingAddress)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Employee inserted")
            flash("Employee inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        except Exception as e:
            print(f'Error {e}')
            flash(e, category = 'error')
        finally:
            cur.close()

    cur = conn.cursor()
    try:
        insertQuery = "select freeApartments();"
        cur.execute(insertQuery)
        apartments = cur.fetchone()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        flash("The operation could not be performed successfully", category = 'error')
    finally:
        cur.close()
    
    return render_template('insert/iEmployee.html', apartmentsNumber = apartments[0])

@insert.route('/lodging', methods = ['GET', 'POST'])
def iLodging():
    if request.method == 'POST':
        address = request.form.get('address')
        apartments = request.form.get('apartments')
        cur = conn.cursor()
            
        try:
            insertQuery = "insert into lodging (address, apartments) values (%s, %s);"
            record = (address, apartments)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Lodging inserted")
            flash("Lodging inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('insert/iLodging.html')

@insert.route('/warehouse', methods = ['GET', 'POST'])
def iWarehouse():
    if request.method == 'POST':
        address = request.form.get('address')
        flower_quantity = request.form.get('flower_quantity')
        seed_quantity = request.form.get('seed_quantity')
        flower_price = request.form.get('flower_price')
        seed_price = request.form.get('seed_price')    
        cur = conn.cursor()

        try:
            insertQuery = "insert into warehouse (address, flower_quantity, seed_quantity, flower_price, seed_price) values (%s, %s, %s, %s, %s);"
            record = (address, flower_quantity, seed_quantity, flower_price, seed_price)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Warehouse inserted")
            flash("Warehouse inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('insert/iWarehouse.html')

@insert.route('/farmland', methods = ['GET', 'POST'])
def iFarmland():
    if request.method == 'POST':
        address = request.form.get('address')
        area = request.form.get('area')
            
        cur = conn.cursor()
        try:
            insertQuery = "insert into farmland (address, area) values (%s, %s);"
            record = (address, area)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Farmland inserted")
            flash("Farmland inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('insert/iFarmland.html')

@insert.route('/client', methods = ['GET', 'POST'])
def iClient():
    if request.method == 'POST':
        pesel = request.form.get('pesel')
        name = request.form.get('name')
        surname = request.form.get('surname')
        company = request.form.get('company')
    
        if any(i.isdigit() for i in name):
            print("Your name cannot conatin digits")
            flash("Your name cannot conatin digits", category = 'error')
        elif any(i.isdigit() for i in surname):
            print("Your surname cannot conatin digits")
            flash("Your surname cannot conatin digits", category = 'error')
            
        cur = conn.cursor()
        try:
            insertQuery = "insert into client (pesel, name, surname, company) values (%s, %s, %s, %s);"
            record = (pesel, name, surname, company)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Client inserted")
            flash("Client inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('insert/iClient.html')

@insert.route('/equipment', methods = ['GET', 'POST'])
def iEquipment():
    if request.method == 'POST':
        name = request.form.get('name')
        model = request.form.get('model')
        warrantyValidity = request.form.get('warranty_validity')

        # the data attribute cannot accept the value ''
        if warrantyValidity == '':
            warrantyValidity = None

        cur = conn.cursor()
        try:
            insertQuery = "insert into equipment (id, name, model, warranty_validity) values (nextval('eq_seq'), %s, %s, %s);"
            record = (name, model, warrantyValidity)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Equipment inserted")
            flash("Equipment inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
        
    return render_template('insert/iEquipment.html')

@insert.route('/sowing', methods = ['GET', 'POST'])
def iSowing():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')
        seed_quantity = request.form.get('seed_quantity')
        equipment_id = request.form.get('equipment_id')
        farmland_address = request.form.get('farmland_address')
        person_pesel = request.form.get('person_pesel')

        cur = conn.cursor()
        try:
            insertQuery = "insert into sowing (recent_activity, seed_quantity, equipment_id, farmland_address, person_pesel) values (%s, %s, %s, %s, %s);"
            record = (recent_activity, seed_quantity, equipment_id, farmland_address, person_pesel)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Sowing inserted")
            flash("Sowing inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
        
    return render_template('insert/iSowing.html')

@insert.route('/harvest', methods = ['GET', 'POST'])
def iHarvest():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')
        flower_quantity = request.form.get('flower_quantity')
        equipment_id = request.form.get('equipment_id')
        farmland_address = request.form.get('farmland_address')
        person_pesel = request.form.get('person_pesel')

        cur = conn.cursor()
        try:
            insertQuery = "insert into harvest (recent_activity, flower_quantity, equipment_id, farmland_address, person_pesel) values (%s, %s, %s, %s, %s);"
            record = (recent_activity, flower_quantity, equipment_id, farmland_address, person_pesel)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Harvest inserted")
            flash("Harvest inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
        
    return render_template('insert/iHarvest.html')

@insert.route('/weeding', methods = ['GET', 'POST'])
def iWeeding():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')
        equipment_id = request.form.get('equipment_id')
        person_pesel = request.form.get('person_pesel')
        farmland_address = request.form.get('farmland_address')

        cur = conn.cursor()
        try:
            insertQuery = "insert into weeding (recent_activity, equipment_id, person_pesel, farmland_address) values (%s, %s, %s, %s);"
            record = (recent_activity, equipment_id, person_pesel, farmland_address)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Weeding inserted")
            flash("Weeding inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
        
    return render_template('insert/iWeeding.html')

@insert.route('/transaction', methods = ['GET', 'POST'])
def iTransaction():
    if request.method == 'POST':
        flower_quantity = request.form.get('flower_quantity')
        seed_quantity = request.form.get('seed_quantity')
        payment = request.form.get('payment')
        date_of_transaction = request.form.get('date_of_transaction')
        client_pesel = request.form.get('client_pesel')
        warehouse_address = request.form.get('warehouse_address')
        person_pesel = request.form.get('person_pesel')

        cur = conn.cursor()
        try:
            insertQuery = "insert into transaction (id, flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel) values (nextval('tr_seq'), %s, %s, %s, %s, %s, %s, %s);"
            record = (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Transaction inserted")
            flash("Transaction inserted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
        
    return render_template('insert/iTransaction.html')
