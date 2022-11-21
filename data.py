import csv, random
from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

bcrypt = Bcrypt()
db.init_app(app)

def main():
  f = open("data.csv")
  reader = csv.reader(f)

  for id,unique,name in reader:
    major_insurance = Major_Insurance(
      id=id,
      unique_id= unique,
      name=name,
      
    )
    db.session.add(major_insurance)
    db.session.commit()

if __name__ == '__main__':
  with app.app_context():
    main()
