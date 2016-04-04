#!/usr/bin/env python
import os
from flask import Flask
from app import create_app, db
from app.models import User, Follow, Post, Comment
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand



app = create_app(os.getenv('SHERRY_BLOG_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow,  Post=Post, Comment=Comment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app = Flask(__name__)
    manager.run()
