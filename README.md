# Steps
1. Installing dependencies: 
```pip3 install -r requirements.txt```
2. Running the server on PORT 8000:
```python3 main.py```

# Prerequisites
1. A MySQL server set up, and within a database, a table named 'user_accounts' with the following parameters:
```
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| username     | varchar(10)  | NO   | PRI | NULL    |       |
| password     | varchar(100) | NO   |     | NULL    |       |
| position     | int          | NO   |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+

```
2. A .env file with the following parameters:
```
MYSQL_USERNAME=<username of mysql>
MYSQL_PASSWORD=<password of the user>
MYSQL_DATABASE=<database name>
APPSECRETKEY=<any string>
SALT=<a salt for passwords>
```
