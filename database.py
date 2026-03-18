# Database Initialization and Models for Pricing Rules and Print Jobs

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URI = 'sqlite:///print_jobs.db'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

class PricingRule(Base):
    __tablename__ = 'pricing_rules'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=sqlalchemy.func.now())

class PrintJob(Base):
    __tablename__ = 'print_jobs'

    id = Column(Integer, primary_key=True)
    job_name = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    pricing_rule_id = Column(Integer, sqlalchemy.ForeignKey('pricing_rules.id'))
    created_at = Column(DateTime, server_default=sqlalchemy.func.now())

# Create tables
def create_tables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()