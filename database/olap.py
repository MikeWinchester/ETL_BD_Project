import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

username_olap = os.getenv('DB_USERNAME_OLAP')
password_olap = os.getenv('DB_PASSWORD_OLAP')
server_olap = os.getenv('DB_SERVER_OLAP')
port_olap = os.getenv('DB_PORT_OLAP')
service_name_olap = os.getenv('DB_SERVICE_NAME_OLAP')

olap_uri = f'oracle+cx_oracle://{username_olap}:{password_olap}@{server_olap}:{port_olap}/?service_name={service_name_olap}'
engine_olap = create_engine(olap_uri)

olap_connection = engine_olap.connect()