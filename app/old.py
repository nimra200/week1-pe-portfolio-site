import os
import datetime
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
	user=os.getenv("MYSQL_USER"),
	password=os.getenv("MYSQL_PASSWORD"),
	host=os.getenv("MYSQL_HOST"),
	port=3306
)
print(mydb)

class TimelinePost(Model):
	name = CharField()
	email = CharField()
	content = TextField()
	created_at = DateTimeField(default=datetime.datetime.now)
	
	class Meta:
		database = mydb
mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="Prairie Dogs - Nimra's portfolio", url=os.getenv("URL"))


@app.route('/hobby')
def hobby():
    return render_template('hobby.html', hobbies=[
        {
            "name": "Board Games",
            "img": "./static/img/hobby-1.jpg"
        },
        {
            "name": "Hiking",
            "img": "./static/img/hobby-2.jpg"
        }
    ])


@app.route('/experience')
def experience():
    return render_template('experience.html', work_experiences=[
        {
            "company": "Meta",
            "title": "Software Engineer Intern",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit.",
            "date": "2023.06 - Present",
            "url": "https://www.google.com/",
        },
        {
            "company": "Apple",
            "title": "Software Engineer Intern",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit.",
            "date": "2021.06 - 2023.05",
            "url": "https://www.google.com/",
        }
    ], education=[
        {
            "school": "ABC College",
            "url": "https://www.google.com/",
            "date": "2019 - 2023",
            "major": "Computer Science",
            "gpa": "4.0/4.0",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit.",
        },
        {
            "school": "AIT-Budapest",
            "url": "https://www.google.com/",
            "date": "2022",
            "major": "Computer Science",
            "gpa": "4.0/4.0",
            "desc": "Study Abroad Program",
        },
    ])


@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
	name = request.form['name']
	email = request.form['email']
	content = request.form['content']
	timeline_post = TimelinePost.create(name=name, email=email, content=content)

	return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
	return {'timeline_posts': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]}
