import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

username_oltp = os.getenv('DB_USERNAME_OLTP')
password_oltp = os.getenv('DB_PASSWORD_OLTP')
server_oltp = os.getenv('DB_SERVER_OLTP')
port_oltp = os.getenv('DB_PORT_OLTP')
service_name_oltp = os.getenv('DB_SERVICE_NAME_OLTP')

oltp_uri = f'oracle+cx_oracle://{username_oltp}:{password_oltp}@{server_oltp}:{port_oltp}/?service_name={service_name_oltp}'
engine_oltp = create_engine(oltp_uri)

oltp_connection = engine_oltp.connect()