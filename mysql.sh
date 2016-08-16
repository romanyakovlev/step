sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE dbfordjango";
mysql -uroot -e "GRANT ALL PRIVILEGES ON dbfordjango.* TO 'admin'@'localhost' IDENTIFIED BY 'pass'";
