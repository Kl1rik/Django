import mysql.connector


def init_db():
    # change host-name for each platform(EX. mysql-pod/mysql-container)
    conn = mysql.connector.connect(
                host='mysql-pod',
                user='test',
                password='testtest',
                database='test'
            )
    cursor = conn.cursor()
    print("init success")
    query = """
            CREATE TABLE Feedback (
                Name CHAR(255),
                AgeGroup CHAR(255),
                Feedback CHAR(255)
                )
            
            """
    
    cursor.execute(query)
    conn.commit()
    conn.close()


init_db()

