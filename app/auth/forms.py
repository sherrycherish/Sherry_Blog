# coding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('邮箱', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[InputRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    email = StringField('邮箱', validators=[InputRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                                                                     'Usernames must have only letters,'
                                                                                    'numbers, dots or underscores')])
    password = PasswordField('密码', validators=[InputRequired(), EqualTo('confirm_password', message='密码必须一致')])
    confirm_password = PasswordField('确认密码', validators=[InputRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在.')


class ChangePasswordForm(Form):
    old_password = PasswordField('旧密码', validators=[InputRequired()])
    password = PasswordField('新密码', validators=[InputRequired(), EqualTo('confirm_password', message='密码必须一致')])
    confirm_password = PasswordField('确认新密码', validators=[InputRequired()])
    submit = SubmitField('更新密码')


class PasswordResetRequestForm(Form):
    email = StringField('邮箱', validators=[InputRequired(), Length(1, 64),
                                          Email()])
    submit = SubmitField('重置密码')


class PasswordResetForm(Form):
    email = SubmitField('邮箱', validators=[InputRequired(), Length(1,64),Email()])
    password = PasswordField('新密码', validators=[
        InputRequired(), EqualTo('confirm_password', message='密码必须一致')])
    confirm_password = PasswordField('确认新密码', validators=[InputRequired()])
    submit = SubmitField('重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('该邮箱未注册')

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)

    sys.setdefaultencoding(default_encoding)




