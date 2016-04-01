#coding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length
from flask.ext.pagedown.fields import PageDownField


class NameForm(Form):
    name = StringField('你的名字是什么?', validators=[InputRequired()])
    submit = SubmitField('提交')


class EditProfileForm(Form):
    name = StringField('真名', validators=[Length(0, 64)])
    location = StringField('住址', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我(介绍你自己)')
    submit = SubmitField('提交')


class PostForm(Form):
    body = PageDownField("说点什么吧:")
    submit = SubmitField('发表')


class CommentForm(Form):
    body = StringField('写下你的评论:')
    submit = SubmitField('发表')
