import os
Agilemanager_collector = {
        'AGM_SERVER': os.getenv("AGM_SERVER", "world"),
        'client_id': os.getenv("CLIENT_ID", "world"),
        'client_secret': os.getenv("CLIENT_SECRET", "world"),
        'db_host': os.getenv("DB_HOST","db"),
        'db_port': 27017
        }
