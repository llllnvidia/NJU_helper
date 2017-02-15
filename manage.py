#!/usr/bin/env python
import os
from app import create_app, db
# from app.models import User, Follow, Role, Permission, Post, Comment
#######
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
# from flask_login import login_manager
# from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    # return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
    #             Permission=Permission, Post=Post, Comment=Comment)
    #########
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))