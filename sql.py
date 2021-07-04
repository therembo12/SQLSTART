import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import *
from psycopg2 import Error
try:
    connection = psycopg2.connect(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database='homeworkSql')

    cursor = connection.cursor()
    # print('Server information:')
    # print(connection.get_dsn_parameters())
    cursor.execute('SELECT VERSION()')
    # print(cursor.fetchone())

    create_table_query = '''CREATE TABLE if not exists homeworkTable3
        (   id SERIAL PRIMARY KEY NOT NULL,
            name TEXT          NOT NULL,
            email TEXT          NOT NULL,
            password INT        NOT NULL
        );
    '''
    add_new_user_qr = """
        INSERT INTO public.homeworktable3
        (
            name,email,password
        )
        VALUES('Bill','Bill@gmail.com','12345678'),
    ('John','John@gmail.com','12345678'),
    ('Gena','Gena@gmail.com','12345678'),
    ('Iyuna','Iyuna@gmail.com','12345678'),
    ('Sanya','Sanya@gmail.com','12345678'),
    ('Andrew','Andrew@gmail.com','12345678'),
    ('Pasha','Pasha@gmail.com','12345678'),
    ('Bill1','Bill1@gmail.com','12345678'),
    ('Bill2','Bill2@gmail.com','12345678'),
    ('Bill3','Bill3@gmail.com','12345678');
    """
    select_by_email_qr = """
        SELECT email from public.homeworktable3 WHERE email like '%yandex%';
    """
    change_pass_qr = """
        UPDATE public.homeworktable3 SET password = '87654321' WHERE id = 4;
    """
    delete_user_qr = """
        DELETE FROM public.homeworktable3 WHERE name like '%Bill%';
    """
    show_user_query = """
        SELECT * from public.homeworktable3 WHERE name like 'A%';
    """
    # cursor.execute(create_table_query)
    # cursor.execute(add_new_user_qr)
    # cursor.execute(select_by_email_qr)
    # cursor.execute(change_pass_qr)
    # cursor.execute(delete_user_qr)
    cursor.execute(show_user_query)
    key = cursor.fetchall()
    print(key)
    connection.commit()
    print('Commit Success')
except(Exception, Error) as error:
    print('Error Connection', error)
finally:
    if connection:
        print('Connection closed')
        cursor.close()
        connection.close()
        # VALUES(1,'Bill','Bill@gmail.com','12345678'),
        # (2,'John','John@gmail.com','12345678'),
        # (3,'Gena','Gena@gmail.com','12345678'),
        # (4,'Iyuna','Iyuna@gmail.com','12345678'),
        # (5,'Sanya','Sanya@gmail.com','12345678'),
        # (6,'Andrew','Andrew@gmail.com','12345678'),
        # (7,'Pasha','Pasha@gmail.com','12345678'),
        # (8,'Bill1','Bill1@gmail.com','12345678'),
        # (9,'Bill2','Bill2@gmail.com','12345678'),
        # (10,'Bill3','Bill3@gmail.com','12345678');
