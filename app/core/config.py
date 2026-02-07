import os

class Settings:
    MYSQL_HOST = os.getenv("MYSQLHOST") or os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQLPORT") or os.getenv("MYSQL_PORT") or 3306)
    MYSQL_USER = os.getenv("MYSQLUSER") or os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD") or os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQLDATABASE") or os.getenv("MYSQL_DATABASE")

settings = Settings()