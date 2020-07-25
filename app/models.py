from app import db


class Plants(db.Model):


    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    imageurl = db.Column(db.String(1000))

    def __init__(self, name=None, imageurl=None):
        self.name = name
        self.imageurl = imageurl