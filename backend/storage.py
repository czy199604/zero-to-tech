import sqlite3


DB_FILE = "history.db"

def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row      # 让查询结果带上列名（默认是元组）
    return conn

#建表语句
def init_db():
    conn = get_conn()
    cur = conn.cursor()
    #表不存在才建，存在了就跳过
    cur.execute("""
    CREATE TABLE IF NOT EXISTS history (   
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        score REAL,
        label TEXT,
        pinyin TEXT,
        created_at TEXT
    )
    """)
    #创建索引，不存在就建，存在就跳过
    cur.execute("CREATE INDEX IF NOT EXISTS idx_history_created ON history(created_at)")
    conn.commit()
    conn.close()




def save_record(record):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO history (text, score, label, pinyin, created_at) VALUES (?, ?, ?, ?, ?)",
        [record["text"], record["score"], record["label"], record["pinyin"], record["created_at"]],
    )
    conn.commit()
    conn.close()



def get_history(limit):#获取指定数量的记录
    conn = get_conn()
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT * FROM history ORDER BY created_at DESC LIMIT ?",
        [limit],
    ).fetchall()
    conn.close()
    #把取到的值转换成比较友好的格式
    records = []
    for row in rows:
        records.append(dict(row))
    return records
