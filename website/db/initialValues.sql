insert into warehouse (address, flower_quantity, seed_quantity, flower_price, seed_price)
values ('Meerweg 44, Breezand', 10, 10, 5, 1);
insert into warehouse (address, flower_quantity, seed_quantity, flower_price, seed_price)
values ('Botsweg 17, Breezand', 100, 100, 50, 15);
insert into lodging (address, apartments)
values ('Zerweg 34, Tzand', 6);
insert into lodging (address, apartments)
values ('Laan 11, Schagen', 3);
insert into person (pesel, name, surname, phone_number, birth_date, salary, role, lodging_address)
values ('12345678901', 'John', 'Doe', 123456789, '1996-12-02', 1000, 'employee', 'Zerweg 34, Tzand');
insert into person (pesel, name, surname, phone_number, birth_date, salary, role, lodging_address)
values ('76200916712', 'Jessica', 'Gomez', 782549267, '1987-06-08', 3000, 'accountant', 'Laan 11, Schagen');
insert into client (pesel, name, surname, company)
values ('76016142947', 'Arnold', 'Ingrid', 'Kapiteyn');
insert into farmland (address, area)
values ('Paal 110, Breezand', 100);
insert into equipment (id, name)
values (nextval('eq_seq'), 'Combine harvester');
insert into equipment (id, name, model)
values (nextval('eq_seq'), 'Sprinkler', '12');
insert into equipment (id, name, model)
values (nextval('eq_seq'), 'Sprinkler', '14');
insert into equipment (id, name, model, warranty_validity)
values (nextval('eq_seq'), 'Tractor', 'LS-305', '2022-07-27');