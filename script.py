import pandas as pd
import time
from sqlalchemy import create_engine

try:
    # Read data from MySQL
    mysql_conn_string = "mysql+mysqlconnector://root:mysql@localhost:3305/operational"
    mysql_engine = create_engine(mysql_conn_string)
    query = "SELECT * FROM youtube;"
    result_dataFrame = pd.read_sql(query, mysql_engine)
    print(result_dataFrame)

    # Write data to PostgreSQL
    postgres_conn_string = "postgresql://postgres:postgres@localhost/data_warehouse"
    postgres_engine = create_engine(postgres_conn_string)

    start_time_mysql = time.time()
    result_dataFrame = pd.read_sql(query, mysql_engine)
    print("MySQL query duration: {} seconds".format(time.time() - start_time_mysql))

    start_time_postgres = time.time()
    result_dataFrame.to_sql('youtube_etl', con=postgres_engine, if_exists='replace', index=False)
    print("to_sql duration: {} seconds".format(time.time() - start_time_postgres))

except Exception as e:
    print(str(e))

pip install pandas mysql-connector-python Flask-SQLAlchemy psycopg2-binary

