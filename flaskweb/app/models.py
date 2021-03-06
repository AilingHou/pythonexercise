from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin 
from . import login_manager

class Role(UserMixin, db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	password_hash = db.Column(db.String(128))
	users = db.relationship('User', backref='role')

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@property.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	def __repr__(self):
		return 'role: %r'% self.name


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)

	def __repr__(self):
		return 'user: %r'% self.username

	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

#db.session.add([])
