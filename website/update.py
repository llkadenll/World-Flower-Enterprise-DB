from flask import Blueprint, render_template, request, flash, redirect, url_for
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

update = Blueprint('update', __name__)

@update.route('/employee', methods = ['GET', 'POST'])
def uEmployee():
    if request.method == 'POST':
        pesel = request.form.get('pesel')
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        birth = request.form.get('birthDate')
        salary = request.form.get('salary')
        role = request.form.get('role')
        lodgingAddress = request.form.get('lodgingAddress')

        cur = conn.cursor()

        record = (name, surname, phone, birth, salary, role, lodgingAddress, pesel)
        indices = [i for i, x in enumerate(record) if x == '' or x == None]

        try:
            insertQuery = 'select name, surname, phone_number, birth_date, salary, role, lodging_address from person where pesel = %s;'
            cur.execute(insertQuery, (pesel,))
            result = cur.fetchone()

            if result == None:
                    flash("Enter the correct pesel", category = 'error')
                    return render_template('update/uEmployee.html')
           
            if indices:              
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)
                
                insertQuery = "update person set (name, surname, phone_number, birth_date, salary, role, lodging_address) = (%s, %s, %s, %s, %s, %s, %s) where pesel = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update person set (name, surname, phone_number, birth_date, salary, role, lodging_address) = (%s, %s, %s, %s, %s, %s, %s) where pesel = %s;"
                record = (name, surname, phone, birth, salary, role, lodgingAddress, pesel)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Employee modified")
            flash('Employee modified', category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uEmployee.html')

@update.route('/warehouse', methods = ['GET', 'POST'])
def uWarehouse():
    if request.method == 'POST':
        address = request.form.get('address')
        flower_quantity = request.form.get('flower_quantity')
        seed_quantity = request.form.get('seed_quantity')
        flower_price = request.form.get('flower_price')
        seed_price = request.form.get('seed_price')
            
        cur = conn.cursor()

        record = (flower_quantity, seed_quantity, flower_price, seed_price, address)
        indices = [i for i, x in enumerate(record) if x == '']

        try:
            insertQuery = "select flower_quantity, seed_quantity, flower_price, seed_price from warehouse where address = %s;"
            cur.execute(insertQuery, (address,))
            result = cur.fetchone()

            if result == None:
                    flash("Enter the correct address", category = 'error')
                    return render_template('update/uWarehouse.html')

            if indices:
                record = list(record)
            
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update warehouse set (flower_quantity, seed_quantity, flower_price, seed_price) = (%s, %s, %s, %s) where address = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
                print("Warehouse updated")
                flash("Warehouse updated", category = 'success')
            else:
                insertQuery = "update warehouse set (flower_quantity, seed_quantity, flower_price, seed_price) = (%s, %s, %s, %s) where address = %s;"
                record = (flower_quantity, seed_quantity, flower_price, seed_price, address)
                cur.execute(insertQuery, record)
                conn.commit()
                print("Warehouse updated")
                flash("Warehouse updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uWarehouse.html')

@update.route('/warehouse/lower', methods = ['GET', 'POST'])
def uWarehouseLower():
    percentage = request.form.get('discount_percentage')
    address = request.form.get('discount_address')
    
    cur = conn.cursor()

    try:
        insertQuery = "select * from warehouse where address = %s;"
        cur.execute(insertQuery, (address,))
        result = cur.fetchone()

        if result == None:
            flash("Enter the correct address", category = 'error')
            return redirect(url_for('.uWarehouse'))

        insertQuery = "call discount(%s, %s);"
        record = (percentage, address)
        cur.execute(insertQuery, record)
        conn.commit()
        print("Flower price updated")
        flash("Flower price updated", category = 'success')
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        flash("The price reduction was not successful", category = 'error')
    finally:
        cur.close()

    return redirect(url_for('select.sWarehouse'))

@update.route('/warehouse/increase', methods = ['GET', 'POST'])
def uWarehouseIncrease():
    percentage = request.form.get('price_increase_percentage')
    address = request.form.get('price_increase_address')
    
    cur = conn.cursor()

    try:
        insertQuery = "select * from warehouse where address = %s;"
        cur.execute(insertQuery, (address,))
        result = cur.fetchone()

        if result == None:
            flash("Enter the correct address", category = 'error')
            return redirect(url_for('.uWarehouse'))

        insertQuery = "call priceIncrease(%s, %s);"
        record = (percentage, address)
        cur.execute(insertQuery, record)
        conn.commit()
        print("Flower price updated")
        flash("Flower price updated", category = 'success')
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        flash("The price increase was not successful", category = 'error')
    finally:
        cur.close()

    return redirect(url_for('select.sWarehouse'))

@update.route('/lodging', methods = ['GET', 'POST'])
def uLodging():
    if request.method == 'POST':
        address = request.form.get('address')
        apartments = request.form.get('apartments')

        cur = conn.cursor()
            
        try:
            insertQuery = "select apartments from lodging where address = %s;"
            cur.execute(insertQuery, (address,))
            result = cur.fetchone()

            if result == None:
                    flash("Enter the correct address", category = 'error')
                    return render_template('update/uLodging.html')

            insertQuery = "update lodging set apartments = %s where address = %s;"
            record = (apartments, address)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Lodging updated")
            flash("Lodging updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    
    return render_template('update/uLodging.html')

@update.route('/farmland', methods = ['GET', 'POST'])
def uFarmland():
    if request.method == 'POST':
        address = request.form.get('address')
        area = request.form.get('area')

        cur = conn.cursor()
            
        try:
            insertQuery = "select area from farmland where address = %s;"
            cur.execute(insertQuery, (address,))
            result = cur.fetchone()

            if result == None:
                    flash("Enter the correct address", category = 'error')
                    return render_template('update/uFarmland.html')

            insertQuery = "update farmland set area = (%s) where address = %s;"
            record = (area, address)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Farmland updated")
            flash("Farmland updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uFarmland.html')

@update.route('/client', methods = ['GET', 'POST'])
def uClient():
    if request.method == 'POST':
        pesel = request.form.get('pesel')
        name = request.form.get('name')
        surname = request.form.get('surname')
        company = request.form.get('company')

        cur = conn.cursor()
        
        record = (name, surname, company, pesel)
        indices = [i for i, x in enumerate(record) if x == '']

        try:
            insertQuery = "select name, surname, company from client where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct pesel", category = 'error')
                return render_template('update/uClient.html')

            if indices:
                record = list(record)
            
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)
            
                insertQuery = "update client set (name, surname, company) = (%s, %s, %s) where pesel = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update client set (name, surname, company) = (%s, %s, %s) where pesel = %s;"
                record = (name, surname, company, pesel)
                cur.execute(insertQuery, record)
                conn.commit()
                
            print("Client modified")
            flash("Client modified", category = 'success')
        except psycopg2.DatabaseError as e:
                print(f'Error {e}')
                flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uClient.html')

@update.route('/equipment', methods = ['GET', 'POST'])
def uEquipment():
    if request.method == 'POST':

        id = request.form.get('id')
        name = request.form.get('name')
        model = request.form.get('model')
        warrantyValidity = request.form.get('warranty_validity')

        cur = conn.cursor()

        record = (name, model, warrantyValidity, id)
        indices = [i for i, x in enumerate(record) if x == '']

        try:
            insertQuery = "select name, model, warranty_validity from equipment where id = %s;"
            cur.execute(insertQuery, (id,))
            result = cur.fetchone()

            if result == None:
                flash("Enter the correct id", category = 'error')
                return render_template('update/uEquipment.html')

            if indices:                
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update equipment set (name, model, warranty_validity) = (%s, %s, %s) where id = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update equipment set (name, model, warranty_validity) = (%s, %s, %s) where id = %s;"
                record = (name, model, warrantyValidity, id)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Equipment modified")
            flash("Equipment modified", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uEquipment.html')

@update.route('/sowing', methods = ['GET', 'POST'])
def uSowing():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')
        seed_quantity = request.form.get('seed_quantity')
        equipment_id = request.form.get('equipment_id')
        farmland_address = request.form.get('farmland_address')
        person_pesel = request.form.get('person_pesel')
        
        cur = conn.cursor()

        record = (seed_quantity, equipment_id, farmland_address, person_pesel, recent_activity)
        indices = [i for i, x in enumerate(record) if x == '']
            
        try:
            insertQuery = "select seed_quantity, equipment_id, farmland_address, person_pesel from sowing where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            result = cur.fetchone()
            
            if result == None:
                flash("Enter the correct date", category = 'error')
                return render_template('update/uSowing.html')

            if indices:
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update sowing set (seed_quantity, equipment_id, farmland_address, person_pesel) = (%s, %s, %s, %s) where recent_activity = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update sowing set (seed_quantity, equipment_id, farmland_address, person_pesel) = (%s, %s, %s, %s) where recent_activity = %s;"
                record = (seed_quantity, equipment_id, farmland_address, person_pesel, recent_activity)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Sowing updated")
            flash("Sowing updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uSowing.html')

@update.route('/harvest', methods = ['GET', 'POST'])
def uHarvest():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')
        flower_quantity = request.form.get('flower_quantity')
        equipment_id = request.form.get('equipment_id')
        farmland_address = request.form.get('farmland_address')
        person_pesel = request.form.get('person_pesel')

        cur = conn.cursor()

        record = (flower_quantity, equipment_id, farmland_address, person_pesel, recent_activity)
        indices = [i for i, x in enumerate(record) if x == '']
            
        try:
            insertQuery = "select flower_quantity, equipment_id, farmland_address, person_pesel from harvest where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            result = cur.fetchone()
            
            if result == None:
                flash("Enter the correct date", category = 'error')
                return render_template('update/uHarvest.html')

            if indices:
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update harvest set (flower_quantity, equipment_id, farmland_address, person_pesel) = (%s, %s, %s, %s) where recent_activity = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update harvest set (flower_quantity, equipment_id, farmland_address, person_pesel) = (%s, %s, %s, %s) where recent_activity = %s;"
                record = (flower_quantity, equipment_id, farmland_address, person_pesel, recent_activity)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Harvest updated")
            flash("Harvest updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uHarvest.html')

@update.route('/weeding', methods = ['GET', 'POST'])
def uWeeding():
    if request.method == 'POST':
        recent_activity = request.form.get('recent_activity')
        equipment_id = request.form.get('equipment_id')
        farmland_address = request.form.get('farmland_address')
        person_pesel = request.form.get('person_pesel')

        cur = conn.cursor()

        record = (equipment_id, person_pesel, farmland_address, recent_activity)
        indices = [i for i, x in enumerate(record) if x == '']
            
        try:
            insertQuery = "select equipment_id, person_pesel, farmland_address from weeding where recent_activity = %s;"
            cur.execute(insertQuery, (recent_activity,))
            result = cur.fetchone()
            
            if result == None:
                flash("Enter the correct date", category = 'error')
                return render_template('update/uWeeding.html')

            if indices:
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update weeding set (equipment_id, person_pesel, farmland_address) = (%s, %s, %s) where recent_activity = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update weeding set (equipment_id, person_pesel, farmland_address) = (%s, %s, %s) where recent_activity = %s;"
                record = (equipment_id, person_pesel, farmland_address, recent_activity)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Weeding updated")
            flash("Weeding updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uWeeding.html')

@update.route('/transaction', methods = ['GET', 'POST'])
def uTransaction():
    if request.method == 'POST':
        id = request.form.get('id')
        flower_quantity = request.form.get('flower_quantity')
        seed_quantity = request.form.get('seed_quantity')
        person_pesel = request.form.get('person_pesel')
        payment = request.form.get('payment')
        date_of_transaction = request.form.get('date_of_transaction')
        client_pesel = request.form.get('client_pesel')
        warehouse_address = request.form.get('warehouse_address')
            
        cur = conn.cursor()

        record = (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel, id)
        indices = [i for i, x in enumerate(record) if x == '']

        try:
            insertQuery = "select flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel from transaction where id = %s;"
            cur.execute(insertQuery, (id,))
            result = cur.fetchone()
            
            if result == None:
                flash("Enter the correct id", category = 'error')
                return render_template('update/uTransaction.html')
                
            if indices:
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update transaction set (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel) = (%s, %s, %s, %s, %s, %s, %s) where id = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update transaction set (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel) = (%s, %s, %s, %s, %s, %s, %s) where id = %s;"
                record = (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel, id)
                cur.execute(insertQuery, record)
                conn.commit()
            
            print("Transaction updated")
            flash("Transaction updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uTransaction.html')