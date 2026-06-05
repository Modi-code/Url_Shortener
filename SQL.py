import sqlite3
def create_table():
    with sqlite3.connect('urls.db') as conn:
        cur=conn.cursor()
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS url(
                    HASH VARCHAR(50) NOT NULL,
                    FHASH VARCHAR(50) NOT NULL,
                    URL VARCHAR(200) NOT NULL UNIQUE,
                    SALT CHAR(32) NOT NULL,
                    PRIMARY KEY(HASH)
                    );
        ''')
        conn.commit()

def insert_URL(HASH,FHASH,URL,SALT):
    with sqlite3.connect('urls.db') as conn:
        cur=conn.cursor()
        cur.execute('SELECT HASH, URL FROM url WHERE URL=?', (URL,))
        result=cur.fetchone()
        if result is not None:
            return True

        success=False
        hash_len=7
        while not success:
            current_hash = FHASH[:hash_len]
            try:
                cur.execute('INSERT INTO url(HASH,FHASH,URL,SALT) VALUES (?, ?, ?, ?)',(current_hash,FHASH,URL,SALT))
                success=True
            except sqlite3.IntegrityError:
                hash_len+=1
                if hash_len>=len(FHASH):
                    break
        return success

def get_URL(HASH):
    with sqlite3.connect('urls.db') as conn:
        cur=conn.cursor()
        cur.execute('SELECT URL FROM url WHERE HASH=?',(HASH,))
        result=cur.fetchone()
        return str(result[0]) if result else None

def reset_table():
    with sqlite3.connect('urls.db') as conn:
        cur=conn.cursor()
        cur.execute('DROP TABLE url')

def url_exists(URL):
    with sqlite3.connect('urls.db') as conn:
        cur=conn.cursor()
        cur.execute('SELECT HASH FROM url WHERE URL=?', (URL,))
        result=cur.fetchone()
        print(result)
        return str(result[0]) if result != None else None
