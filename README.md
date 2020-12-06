# Steps
1. Installing dependencies: 
```pip3 install -r requirements.txt```
2. Running the server on PORT 5000:
```python3 main.py```

# Prerequisites
1. A MySQL server set up, and within a database, a table named 'user' with the following parameters:
```
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| email        | varchar(255) | NO   | PRI | NULL    |       |
| name         | varchar(255) | NO   |     | NULL    |       |
| company_name | varchar(255) | NO   |     | NULL    |       |
| mobile_no    | bigint       | NO   |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+

```
2. A .env file with the following parameters:
```
MYSQL_USERNAME=<username of mysql>
MYSQL_PASSWORD=<password of the user>
MYSQL_DATABASE=<database name>
```
3. The API endpoints are:
```
/create: POST only
/update: POST only
/list: GET only
/delete: POST only
```
4. All requests made to the server should have a content-type of application/json
5. The format of the JSON requests has to be:
```
{
    "name": "name",
    "email": "email",
    "company_name": "company name",
    "mobile_no": phone_no 
}
```