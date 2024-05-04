CREATE DATABASE firearms_data;

USE firearms_data;

CREATE TABLE firearms (
  id INT AUTO_INCREMENT PRIMARY KEY,
  anime_character VARCHAR(255),
  firearm_name VARCHAR(255),
  firearm_type VARCHAR(255),
  firearm_manufacturer VARCHAR(255),
  firearm_caliber VARCHAR(255),
  firearm_capacity INT,
  firearm_length FLOAT,
  firearm_weight FLOAT,
  firearm_features TEXT
);