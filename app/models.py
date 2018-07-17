from app import db


class ExampleModel(db.Model):
    __tablename__ = 'example_model'

    id = db.Column(db.Integer, primary_key=True)
    value_column = db.Column(db.String())

    def __init__(self, value_column):
        self.value_column = value_column

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<id {}>'.format(self.id)
