
# -*- coding: utf-8 -*-

import psycopg2
import asyncio
import json
import os

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

conn = psycopg2.connect(
    dbname=POSTGRES_DB, 
    user=POSTGRES_USER, 
    host=POSTGRES_HOST, 
    port=POSTGRES_PORT, 
    password=POSTGRES_PASSWORD
)

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()

def listen(channel):
    def decorator(handle):
        
        cursor.execute(f"LISTEN {channel};")

        def notify():
            conn.poll()
            
            for notify in conn.notifies:
                handle(notify.channel, notify.payload)

            conn.notifies.clear()

        loop = asyncio.get_event_loop()
        loop.add_reader(conn, notify)
        loop.run_forever()

    return decorator




