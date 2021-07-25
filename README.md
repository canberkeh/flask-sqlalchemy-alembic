# flask-sqlalchemy-alembic

# 1 - Alembic init 
>> alembic init alembic 

# 2 - Set alembic.ini 
sqlalchemy.url = sqlite:///database.db

# 3 - Create model.py 
engine = create_engine('sqlite:///database.db')
Base = declarative_base()
metadata = Base.metadata

# 4 - Set env.py in alembic folder
from model import Base
target_metadata = [Base.metadata]

# 5 - Generate first migration 
alembic revision --autogenerate -m "initial commit"

# 6 - Generate tables in databse with upgrade 
alembic upgrade head 