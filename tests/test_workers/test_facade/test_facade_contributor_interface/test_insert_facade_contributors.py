from tests.test_workers.worker_persistance.util_persistance import *
from tests.test_workers.test_facade.test_facade_contributor_interface.test_endpoints import set_up_repo_groups

#Use some of facade's methods to get commit data.
from workers.facade_worker.facade_worker import *


def test_insert_facade_contributors_default_basic(database_connection, set_up_repo_groups):
    #set_up_repo_groups(database_connection)
    
    dummy = DummyFullWorker(database_connection)

    #insert some commit data expected one level above augur root directory
    insert_sql_file(dummy.db, "../commits.sql")
    
    dummy.insert_facade_contributors('10')
    dummy.insert_facade_contributors('20')