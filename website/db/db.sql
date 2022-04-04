create table client (
    pesel    VARCHAR(11) NOT NULL,
    name     VARCHAR(20) NOT NULL,
    surname  VARCHAR(30) NOT NULL,
    company  VARCHAR(30)
);

create table equipment (
    id    INTEGER NOT NULL,
    name     VARCHAR(20) NOT NULL,
    model  VARCHAR(25),
    warranty_validity DATE
);

create table person (
    pesel            VARCHAR(11) NOT NULL,
    name             VARCHAR(20) NOT NULL,
    surname          VARCHAR(30) NOT NULL,
    phone_number     VARCHAR(9) NOT NULL,
    birth_date       DATE NOT NULL,
    salary           FLOAT(2) NOT NULL,
    role             VARCHAR(10) NOT NULL,
    lodging_address  VARCHAR(35) NOT NULL
);

create table lodging (
    address     VARCHAR(35) NOT NULL,
    apartments  INTEGER NOT NULL
);

create table warehouse (
    address          VARCHAR(35) NOT NULL,
    flower_quantity  INTEGER NOT NULL,
    seed_quantity    FLOAT(2) NOT NULL,
    flower_price     FLOAT(2) NOT NULL,
    seed_price       FLOAT(2) NOT NULL
);

create table farmland (
    address  VARCHAR(35) NOT NULL,
    area     NUMERIC(6, 2) NOT NULL
);

create table transaction (
    id                   INTEGER NOT NULL,
    flower_quantity      INTEGER NOT NULL,
    seed_quantity        FLOAT(2) NOT NULL,
    payment              FLOAT(2) NOT NULL,
    date_of_transaction  DATE NOT NULL,
    client_pesel         VARCHAR(11) NOT NULL,
    warehouse_address    VARCHAR(35) NOT NULL,
    person_pesel         VARCHAR(11) NOT NULL
);

create table sowing (
    recent_activity   DATE NOT NULL,
    seed_quantity     FLOAT(2) NOT NULL,
    equipment_id      INTEGER NOT NULL,
    farmland_address  VARCHAR(35) NOT NULL,
    person_pesel      VARCHAR(11) NOT NULL
);

create table weeding (
    recent_activity   DATE NOT NULL,
    equipment_id      INTEGER NOT NULL,
    person_pesel      VARCHAR(11) NOT NULL,
    farmland_address  VARCHAR(35) NOT NULL
);

create table harvest (
    recent_activity   DATE NOT NULL,
    flower_quantity   INTEGER NOT NULL,
    equipment_id      INTEGER NOT NULL,
    farmland_address  VARCHAR(35) NOT NULL,
    person_pesel      VARCHAR(11) NOT NULL
);

ALTER TABLE client ADD CONSTRAINT client_pk PRIMARY KEY ( pesel );

ALTER TABLE equipment ADD CONSTRAINT equipment_pk PRIMARY KEY ( id );

ALTER TABLE farmland ADD CONSTRAINT farmland_pk PRIMARY KEY ( address );

ALTER TABLE harvest
    ADD CONSTRAINT harvest_pk PRIMARY KEY ( recent_activity,
                                            equipment_id,
                                            farmland_address,
                                            person_pesel );
											
ALTER TABLE lodging ADD CONSTRAINT lodging_pk PRIMARY KEY ( address );

ALTER TABLE person ADD CONSTRAINT person_pk PRIMARY KEY ( pesel );

ALTER TABLE sowing
    ADD CONSTRAINT sowing_pk PRIMARY KEY ( recent_activity,
                                           equipment_id,
                                           farmland_address,
                                           person_pesel );
										   
ALTER TABLE transaction
    ADD CONSTRAINT transaction_pk PRIMARY KEY ( id,
                                                client_pesel,
                                                warehouse_address,
                                                person_pesel );
												
ALTER TABLE warehouse ADD CONSTRAINT warehouse_pk PRIMARY KEY ( address );

ALTER TABLE weeding
    ADD CONSTRAINT weeding_pk PRIMARY KEY ( recent_activity,
                                            equipment_id,
                                            farmland_address );

ALTER TABLE harvest
    ADD CONSTRAINT harvest_equipment_fk FOREIGN KEY ( equipment_id )
        REFERENCES equipment ( id );

ALTER TABLE harvest
    ADD CONSTRAINT harvest_farmland_fk FOREIGN KEY ( farmland_address )
        REFERENCES farmland ( address );

ALTER TABLE harvest
    ADD CONSTRAINT harvest_person_fk FOREIGN KEY ( person_pesel )
        REFERENCES person ( pesel );

ALTER TABLE person
    ADD CONSTRAINT person_lodging_fk FOREIGN KEY ( lodging_address )
        REFERENCES lodging ( address );

ALTER TABLE sowing
    ADD CONSTRAINT sowing_equipment_fk FOREIGN KEY ( equipment_id )
        REFERENCES equipment ( id );

ALTER TABLE sowing
    ADD CONSTRAINT sowing_farmland_fk FOREIGN KEY ( farmland_address )
        REFERENCES farmland ( address );

ALTER TABLE sowing
    ADD CONSTRAINT sowing_person_fk FOREIGN KEY ( person_pesel )
        REFERENCES person ( pesel );

ALTER TABLE transaction
    ADD CONSTRAINT transaction_client_fk FOREIGN KEY ( client_pesel )
        REFERENCES client ( pesel );

ALTER TABLE transaction
    ADD CONSTRAINT transaction_person_fk FOREIGN KEY ( person_pesel )
        REFERENCES person ( pesel );

ALTER TABLE transaction
    ADD CONSTRAINT transaction_warehouse_fk FOREIGN KEY ( warehouse_address )
        REFERENCES warehouse ( address );

ALTER TABLE weeding
    ADD CONSTRAINT weeding_equipment_fk FOREIGN KEY ( equipment_id )
        REFERENCES equipment ( id );

ALTER TABLE weeding
    ADD CONSTRAINT weeding_farmland_fk FOREIGN KEY ( farmland_address )
        REFERENCES farmland ( address );

ALTER TABLE weeding
    ADD CONSTRAINT weeding_person_fk FOREIGN KEY ( person_pesel )
        REFERENCES person ( pesel );
    
alter table person add check(role in ('worker', 'accountant'));

create sequence tr_seq
start with 1
increment by 1;

create sequence eq_seq
start with 1
increment by 1;

create or replace procedure discount (
    reductionPercentage in float, warehouse_address in varchar)
language plpgsql    
as $$
begin
 update warehouse
 set flower_price = flower_price * (100 - reductionPercentage) / 100
 where address = warehouse_address;
end$$;
-- call discount(10, 'Meerweg 44, Breezand');

create or replace procedure priceIncrease (
    increasePercentage in float, warehouse_address in varchar)
language plpgsql    
as $$
begin
 update warehouse
 set flower_price = flower_price * (100 + increasePercentage) / 100
 where address = warehouse_address;
end$$;
-- call priceIncrease(10, 'Meerweg 44, Breezand');

create or replace function freeApartments ()
returns integer as $counter$
declare
	counter integer;
begin
	select (
		select sum(apartments)
		from lodging
	) - count(*)
	into counter
	from person p join lodging l
	on p.lodging_address = l.address;
   return counter;
end;
$counter$ language plpgsql;
-- select freeApartments();

create or replace function currentFreeApartments (varchar)
returns integer as $counter$
declare
	counter integer;
begin
	select (
		select apartments
		from lodging
		where address = $1
	) - (
		select count(*)
		from person
		where lodging_address = $1
	)
	into counter
	from person p join lodging l
	on p.lodging_address = l.address;
   return counter;
end;
$counter$ language plpgsql;
<<<<<<< HEAD
-- select currentFreeApartments('Laan 11, Schagen');
=======
-- select currentFreeApartments('Laan 11, Schagen');
>>>>>>> 382c61826fb99a7c6e45958c1d3415b2ccaae44d
