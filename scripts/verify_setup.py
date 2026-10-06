"""Week 0 setup check: MySQL tables, sold-data date range, and Gemini API key."""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

ok = True


def report(name: str, passed: bool, detail: str = "") -> None:
    global ok
    ok &= passed
    print(f"[{'PASS' if passed else 'FAIL'}] {name}{' - ' + detail if detail else ''}")


# MySQL
try:
    import mysql.connector

    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )
    cur = conn.cursor()
    for table in ("rets_property", "california_sold"):
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = cur.fetchone()[0]
        report(f"table {table}", count > 0, f"{count:,} rows")
    cur.execute("SELECT MIN(CloseDate), MAX(CloseDate) FROM california_sold")
    first, last = cur.fetchone()
    report("california_sold date range", bool(last), f"{first} -> {last}")
    conn.close()
except Exception as e:
    report("MySQL connection", False, str(e))

# Gemini
try:
    from google import genai

    client = genai.Client()  # reads GEMINI_API_KEY
    emb = client.models.embed_content(model="gemini-embedding-001", contents="3 bed condo in Irvine")
    report("Gemini embeddings", True, f"dim={len(emb.embeddings[0].values)}")
    resp = client.models.generate_content(model="gemini-2.5-flash", contents="Reply with just: ok")
    report("Gemini generation", bool(resp.text), resp.text.strip())
except Exception as e:
    report("Gemini API", False, str(e))

sys.exit(0 if ok else 1)
