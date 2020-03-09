from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
jobs_dict = {}


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', jobs=jobs_dict)


def main():
    global jobs_dict
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()

    for job in session.query(Jobs).all():
        jobs_dict[job.id] = [job.title_of_activity, job.team_leader,
                             job.duration, job.collaborators, job.is_finished]

    app.run(port="8000", host="127.0.0.1")


if __name__ == '__main__':
    main()