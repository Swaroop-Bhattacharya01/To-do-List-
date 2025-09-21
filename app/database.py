import os
import urllib.parse
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# For local development, force SQLite usage by not loading Postgres env vars
# Comment out the lines below if you want to use PostgreSQL
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD_RAW = os.getenv("DB_PASSWORD")
# DB_PASSWORD = urllib.parse.quote_plus(DB_PASSWORD_RAW) if DB_PASSWORD_RAW else None
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# Force None values to use SQLite fallback
DB_USER = None
DB_PASSWORD = None
DB_HOST = None
DB_PORT = None
DB_NAME = None

# Debug print to see what environment variables are loaded
print(f"DB_USER={DB_USER}")
print(f"DB_PASSWORD={'*' * len(DB_PASSWORD) if DB_PASSWORD else None}")
print(f"DB_HOST={DB_HOST}")
print(f"DB_PORT={DB_PORT}")
print(f"DB_NAME={DB_NAME}")

# Determine whether Postgres configuration is complete
is_postgres_configured = all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME])
print(f"Postgres configured: {is_postgres_configured}")

if is_postgres_configured:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print("Using PostgreSQL database")
else:
    # Fallback to local SQLite for development if Postgres env vars are not set
    project_root = Path(__file__).resolve().parent.parent
    sqlite_path = project_root / "app.db"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_path.as_posix()}"
    print(f"Using SQLite database: {SQLALCHEMY_DATABASE_URL}")

# Create the SQLAlchemy engine
connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, connect_args=connect_args)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models to inherit
Base = declarative_base()
