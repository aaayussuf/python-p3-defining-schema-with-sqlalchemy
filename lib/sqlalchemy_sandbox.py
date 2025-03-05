#!/usr/bin/env python3

# Import necessary modules
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'  # Name of the table in the database

    id = Column(Integer(), primary_key=True)  # Primary key column
    name = Column(String())  # Name column

# Ensure script execution only runs when executed directly
if __name__ == '__main__':
    # Create an SQLite database engine
    engine = create_engine('sqlite:///students.db')
    
    # Create the table(s) in the database
    Base.metadata.create_all(engine)
    
    print("Database and students table created successfully!")