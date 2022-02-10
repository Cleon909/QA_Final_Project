#define classes for database
from app import db 


class Academics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    current_insitution = db.Column(db.String(30), default='Unkown')
    field_of_study = db.Column(db.String(30), default='Unkown') # this line could be moved to a seperate table
    authors = db.relationship('Authors', backref = 'academicbr')

    def __init__(self, name, last_name, current_insitution = None, field_of_study = None):
        self.name = name
        self.current_insitution = current_insitution
        self.field_of_study = field_of_study

class Papers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year_published = db.Column(db.Integer)
    impact = db.Column(db.Integer, default=0)
    field_of_study = db.Column(db.String(50), default='Unkown') # this line could be moved to a seperate table
    authors = db.relationship('Authors', backref = 'papersbr')

    def __init__(self, title, year_published, field_of_study):
        self.title = title
        self.year_published = year_published
        self.field_of_study = field_of_study

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academic_id = db.Column(db.Integer, db.ForeignKey('academics.id'), nullable=False) 
    paper_id = db.Column(db.Integer, db.ForeignKey('papers.id'), nullable=False) 

    def __init__(self, academic_id, paper_id):
        self.academic_id = academic_id
        self.paper_id = paper_id

