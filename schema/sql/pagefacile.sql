
#table that will hold the data about what are the types of entities
CREATE  TABLE `pagefacile`.`entity_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(45) NULL ,
  `url` VARCHAR(65) NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `url_UNIQUE` (`url`) ) ENGINE=INNODB;

#table for attributes/properties
CREATE TABLE `pagefacile`.`property` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`label` VARCHAR(45) NULL ,
	PRIMARY KEY (`id`) ,
	UNIQUE INDEX `label_UNIQUE` (`label`) 

) ENGINE=INNODB;


#table for which entity type has which properties
CREATE TABLE `pagefacile`.`property_in_entity` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`entity_type_id` INT NOT NULL,
	`property_id`  INT NOT NULL,
	PRIMARY KEY (`id`) ,
	INDEX `etid_index` (`entity_type_id`),
	INDEX `pid_index` (`property_id`)
)  ENGINE=INNODB;

#table for entity instances
CREATE TABLE `pagefacile`.`entity_data` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`entity_type_id` INT NOT NULL,
	PRIMARY KEY (`id`) ,
	INDEX `etid_data_index` (`entity_type_id`)
) ENGINE=INNODB;

####################################################################

#these are the tables that should be generated for each property
#table for name property value 
CREATE TABLE `pagefacile`.`prop_name_data` (
	`id` INT NOT NULL  AUTO_INCREMENT,
	`entity_data_id` INT NOT NULL,
	`value` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`) ,
	INDEX `edid_name_index` (`entity_data_id`),
	INDEX `prop_name_index` (`value`)

) ENGINE=INNODB;

#table for email property value 
CREATE TABLE `pagefacile`.`prop_email_data` (
	`id` INT NOT NULL  AUTO_INCREMENT,
	`entity_data_id` INT NOT NULL,
	`value` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`id`) ,
	INDEX `edid_email_index` (`entity_data_id`),
	INDEX `prop_email_index` (`value`)

) ENGINE=INNODB;

#table for gender property value 
CREATE TABLE `pagefacile`.`prop_gender_data` (
	`id` INT NOT NULL  AUTO_INCREMENT,
	`entity_data_id` INT NOT NULL,
	`value` VARCHAR(10) NOT NULL,
	PRIMARY KEY (`id`) ,
	INDEX `edid_gender_index` (`entity_data_id`),
	INDEX `prop_gender_index` (`value`)

) ENGINE=INNODB;

