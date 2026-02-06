import os

class Settings:
    MYSQL_HOST = os.getenv("MYSQLHOST")
    MYSQL_PORT = os.getenv("MYSQLPORT")
    MYSQL_USER = os.getenv("MYSQLUSER")
    MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQLDATABASE")

settings = Settings()