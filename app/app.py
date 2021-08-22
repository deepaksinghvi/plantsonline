import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



#database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
#    dbuser=os.environ['DB_USER'],
#    dbpass=os.environ['DB_PASS'],
#    dbhost=os.environ['DB_HOST'],
#    dbname=os.environ['DB_NAME']
#)

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser='postgres',
    dbpass='changeme',
    dbhost='postgres',
    dbname='postgres'
)

app = Flask(__name__)
app.debug = True
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

from models import *

#migrate = Migrate(app, db)
app.logger.info('Init DB')
db.init_app(app)
app.logger.info('creating all started')
db.create_all()
#db.session.commit()
app.logger.info('creating all completed')
# initialize database migration management



@app.route('/')
def view_plants():
    from models import Plants
    plants = Plants.query.all()
    return render_template('plant_list.html', plants=plants)

@app.route('/addplant', methods=['GET'])
def view_registration_form():
    return render_template('plant_add.html')


@app.route('/addplant', methods=['POST'])
def add_plant():
    from models import Plants
    name = request.form.get('name')
    imageurl = request.form.get('imageurl')

    plant = Plants(name, imageurl)
    db.session.add(plant)
    db.session.commit()

    plants = Plants.query.all()
    return render_template('plant_list.html', plants=plants)

@app.route('/addplanttest1', methods=['POST'])
def add_plant():
    from models import Plants
    name = request.form.get('name')
    imageurl = request.form.get('imageurl')

    plant = Plants(name, imageurl)
    db.session.add(plant)
    db.session.commit()

    plants = Plants.query.all()
    return render_template('plant_list.html', plants=plants)

@app.route('/addplanttest2', methods=['POST'])
def add_plant():
    from models import Plants
    name = request.form.get('name')
    imageurl = request.form.get('imageurl')

    plant = Plants(name, imageurl)
    db.session.add(plant)
    db.session.commit()

    plants = Plants.query.all()
    return render_template('plant_list.html', plants=plants)
