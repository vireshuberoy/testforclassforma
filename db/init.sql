CREATE DATABASE classforma;
USE classforma;

CREATE TABLE `user_accounts` (
  `username` varchar(10) primary key,
  `password` varchar(100),
  `position` int
);
