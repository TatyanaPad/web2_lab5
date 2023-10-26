import mysql.connector
from flask import g # импортируем для переменной, в которой будут храниться данные для текущего запроса

class MySQL:
	def __init__(self, app):
		self.app = app
		self.app.teardown_appcontext(self.close_connection)

	def config(self):
		return {
            "user": self.app.config['MYSQL_USER'],
            "password": self.app.config['MYSQL_PASSWORD'],
            "host": self.app.config['MYSQL_HOST'],
            "database": self.app.config['MYSQL_DATABASE'],
			"port": self.app.config['MYSQL_PORT']
        }

	def close_connection(self, e=None):
		db = g.pop('db', None)
		if db is not None:
			db.close()

	def connection(self):
		if 'db' not in g:
			g.db = mysql.connector.connect(**self.config())
		return g.db