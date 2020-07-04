CREATE DATABASE IF NOT EXISTS django_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'django_user'@'%' IDENTIFIED BY 'djangopass';
GRANT ALL PRIVILEGES ON django_db.* TO 'django_user'@'%';

FLUSH PRIVILEGES;
