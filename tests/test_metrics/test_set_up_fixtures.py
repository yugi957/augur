from tests.test_workers.test_set_up_fixtures import *

@pytest.fixture(scope="session")
def augur_app():

    config = {
        "Database": {
            "name": "test",
            "host": "172.17.0.1",
            "password": "augur",
            "port": 5400,
            "user": "augur",
            "database": "test"
        }
    }

    augur_app = Application(given_config=config, disable_logs=True)

    return augur_app

@pytest.fixture(scope="session")
def metrics(augur_app, db_with_default_data):
    return augur_app.metrics


@pytest.fixture(scope="session")
def db_with_default_data(database_connection):

    insert_sql_file(database_connection, "augur_test_data.sql")


def insert_sql_file(database_connection, fileString):
    fd = open(fileString, 'r')

    sqlFile = fd.read()
    fd.close()

    # Get list of commmands
    sqlCommands = sqlFile.split(';')

    # Iterate and execute
    for command in sqlCommands:
        toExecute = s.sql.text(command)
        try:
            database_connection.read_sql(
                toExecute, database_connection, params={})
        except Exception as e:
            print(f"Error when inserting data: {e}")
            