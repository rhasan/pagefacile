INSERT INTO entity_type(label,url) VALUES("Person","http://schema.org/Person");

INSERT INTO property(label) VALUES("name");
INSERT INTO property(label) VALUES("email");
INSERT INTO property(label) VALUES("gender");

INSERT INTO property_in_entity(entity_type_id,property_id) VALUES(1,1);
INSERT INTO property_in_entity(entity_type_id,property_id) VALUES(1,2);
INSERT INTO property_in_entity(entity_type_id,property_id) VALUES(1,3);



#instance data
#entity instance data
INSERT INTO entity_data(entity_type_id) VALUES(1);

#name property instance data
INSERT INTO prop_name_data(entity_data_id,value) VALUES(1,"Alice");
INSERT INTO prop_email_data(entity_data_id,value) VALUES(1,"alice@email.com");
INSERT INTO prop_gender_data(entity_data_id,value) VALUES(1,"Female");



#entity instance data
INSERT INTO entity_data(entity_type_id) VALUES(1);

#name property instance data
INSERT INTO prop_name_data(entity_data_id,value) VALUES(2,"Bob");
INSERT INTO prop_email_data(entity_data_id,value) VALUES(2,"bob@email.com");
INSERT INTO prop_gender_data(entity_data_id,value) VALUES(2,"Male");