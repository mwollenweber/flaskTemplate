__author__ = 'mjw'

import sys
import argparse
import traceback
import datetime
import config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
DEBUG = True

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
db_session._model_changes = {}

Base = declarative_base()
Base.query = db_session.query_property()



def init_db():
    import auth.models

    Base.metadata.create_all(bind=engine)


def main():
    parser = argparse.ArgumentParser(prog='template', usage='%(prog)s [options]')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--version', action='version', version='%(prog)s -1.0')
    parser.add_argument('--debug', '-D', type=bool, dest='DEBUG', default=False)

    args = parser.parse_args()
    DEBUG = args.DEBUG

    try:
        init_db()

    except KeyboardInterrupt:
        sys.exit(-1)

    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()
