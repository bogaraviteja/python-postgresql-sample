import psycopg2
import psycopg2.extras

hostname='localhost'
database='postgres'
username='postgres'
pwd='ravi'
port_id='5432'

conn=None
cur=None

try:
    conn=psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DROP TABLE IF EXISTS employee')

    create_script=''' CREATE TABLE IF NOT EXISTS employee(
                           id int PRIMARY KEY,
                           name varchar(40) NOT NULL,
                           salary int,
                           dept_id varchar(30))'''
    cur.execute(create_script)
    
    insert_script='INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'

    #for inserting single record
    insert_value=(1,'ravi',50000,25)
    cur.execute(insert_script, insert_value)

    # for inserting multiple records
    insert_values=[(2,'sumanth',20000,25),(3,'uday',50000,'d23'),(4,'rakesh',15000,'d24')]
    for record in insert_values:
        cur.execute(insert_script, record)

    # Fetching the data from a table employee in a tuple format
    # In below statement the SELECT statement is fetching data in a single as it is tuple
    cur.execute('SELECT * FROM EMPLOYEE')
    print(cur.fetchall())

    # In below statement the SELECT statement is fetching data in a multiple rows 
    cur.execute('SELECT * FROM EMPLOYEE')
    for record in cur.fetchall(): 
        print(record)

    # In below statement the SELECT statement is fetching data in a multiple rows for specific columns
    cur.execute('SELECT * FROM EMPLOYEE')
    for record in cur.fetchall(): 
        print(record[1], record[3])

    # UPDATE statement 
    update_script='UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)

    '''In below statement the SELECT statement is fetching data for particular column in a by column 
    by name in case if we have large scale of columns'''

    cur.execute('SELECT * FROM EMPLOYEE')
    for record in cur.fetchall(): 
        print(record['name'], record['salary'])

    delete_script='DELETE FROM employee WHERE name=%s'
    delete_value=('rakesh',)
    cur.execute(delete_script,delete_value)

    conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()