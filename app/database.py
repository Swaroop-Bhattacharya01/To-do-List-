import os
import urllib.parse
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Load PostgreSQL environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD_RAW = os.getenv("DB_PASSWORD")
DB_PASSWORD = urllib.parse.quote_plus(DB_PASSWORD_RAW) if DB_PASSWORD_RAW else None
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# For Vercel, also check for DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Debug print to see what environment variables are loaded
print(f"DB_USER={DB_USER}")
print(f"DB_PASSWORD={'*' * len(DB_PASSWORD) if DB_PASSWORD else None}")
print(f"DB_HOST={DB_HOST}")
print(f"DB_PORT={DB_PORT}")
print(f"DB_NAME={DB_NAME}")

# Determine database URL
if DATABASE_URL:
    # Vercel provides DATABASE_URL directly
    SQLALCHEMY_DATABASE_URL = DATABASE_URL
    print("Using DATABASE_URL from environment")
elif all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    # Manual PostgreSQL configuration
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print("Using PostgreSQL database with manual configuration")
else:
    # Fallback to local SQLite for development
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
