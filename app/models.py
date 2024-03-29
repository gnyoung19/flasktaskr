# models.py


from views import db


class Task(db.Model):
	
	__tablename__ = "tasks"
	
	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	due_date = db.Column(db.Date, nullable=False)
	priority = db.Column(db.Integer, nullable=False)
	status = db.Column(db.Integer)
	
	def __init__(self, name, due_date, priority, status):
		self.name = name
		self.due_date = due_date
		self.priority = priority
		self.status = status
		
	def __repr__(self):
		return '<name %r>' % (self.body)
		
class User(db.Model):
	
	__tablename_ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	
	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password
		
	def __repr__(self):
		return '<User %r>' % (self.name)
		
		