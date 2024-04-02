def extract_data(connection):
    cursor = connection.cursor()
    cursor.execute()
    return cursor.fetchall()

def transform_data(data):
    return data

def load_data(connection, data):
    cursor = connection.cursor()
    cursor.executemany()
    connection.commit()