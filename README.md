# Music Classifer by Aiden Zhang
This is a web application built using the Flask boilerplate code provided by MLH. The machine learning model was 
created using Fast.ai, a higher level API built on top of Pytorch (similar relationship as Keras to Tensorflow from 
my understanding). The model was fine-tuned from a RESNET-34 model and dataset used was the GTZAN dataset. 

Note that I was unable to use the original Mel spectrograms from the dataset as I was unable to reproduce similar 
spectrograms using the librosa python module from my end (needed to analyze youtube videos). As such, I created my 
own spectrograms by converting the original audio files from the GTZAN dataset using my own script named 
`gtzanToSpec.py`.


More information about the Machine Learning part of this project can be found [here](https://github.com/waiden674/music_classifier_ML)

### Future Plans
Currently, the model can only classify between 3 of the original 10 genres in GTZAN dataset due to the fact that it 
would take too long for me to train all 10 in a free-tier Google Colab. Perhaps in the future, I will find a work 
around that will allow the model to classify between more genres.


### Below is the installation process from the original MLH Flask boilerplate.


# Introduction

This is a hackathon boilerplate for new Flask web applications created by [Major League Hacking](https://github.com/MLH). It is for hackers looking to get started quickly on a new hackathon project using the Flask microframework.

- [Installation Guide](#installation-guide) - How to get started with a new Flask app
- [User Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md) - How to develop apps created with this starter project
- [Contributing Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/CONTRIBUTING.md) - How to contribute to the project

# <a name='installation-guide'>Installation Guide</a>

This project requires the following tools:

- Python - The programming language used by Flask.
- PostgreSQL - A relational database system.
- Virtualenv - A tool for creating isolated Python environments.

To get started, install Python and Postgres on your local computer if you don't have them already. A simple way for Mac OS X users to install Postgres is using [Postgres.app](https://postgresapp.com/). You can optionally use another database system instead of Postgres, like [SQLite](http://flask.pocoo.org/docs/1.0/patterns/sqlite3/).

## Getting Started

**Step 1. Clone the code into a fresh folder**

```
$ git clone https://github.com/MLH/mlh-hackathon-flask-starter.git
$ cd mlh-hackathon-flask-starter
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new Virtual Environment for the project and activate it. If you don't have the `virtualenv` command yet, you can find installation [instructions here](https://virtualenv.readthedocs.io/en/latest/). Learn more about [Virtual Environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).

```
$ virtualenv venv
$ source venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```

**Step 3: Create an app on GitHub**

Head over to [GitHub OAuth apps](https://github.com/settings/developers) and create a new OAuth app. Name it what you like but you'll need to specify a callback URL, which should be something like:

```
http://localhost:5000/auth/callback/github
```

The default port for Flask apps is `5000`, but you may need to update this if your setup uses a different port or if you're hosting your app somewhere besides your local machine.

**Step 4: Setup your database**

You need to be able to connect to a database either on your own computer (locally) or through a hosted database. You can [install Postgres locally](http://www.postgresqltutorial.com/install-postgresql/) and [connect to it](http://www.postgresqltutorial.com/connect-to-postgresql-database/) to provide the database for your app.

You will need to know the connection URL for your application which we will call `DATABASE_URL` in your environment variables. Here is an example:

```
postgresql://localhost:5432/mlh-hackathon-starter-flask
```

**Step 5: Update environment variables and run the Server.**

Create a new file named `.env` by duplicating `.env.example`. Update the new file with the GitHub credentials. It should look similar to this:

```
# .env file
DATABASE_URL="[INSERT_DATABASE_URL]"
GITHUB_CLIENT_ID="[INSERT_CLIENT_ID]"
GITHUB_CLIENT_SECRET="[INSERT_CLIENT_SECRET]"
```

You replace the GitHub credentials here and update the database URL. Learn more about the required [Environment Variables here](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md#environment-variables).

Now we're ready to start our server which is as simple as:

```
(venv) $ flask run
```

Open http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

# What's Included?

- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - A Flask extension for making modular applications
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - A Flask extension that adds ORM support for your data models.
- [Werkzeug](http://werkzeug.pocoo.org/) - A Flask framework that implements WSGI for handling requests.
- [Bootstrap 4](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.

# Code of Conduct

We enforce a Code of Conduct for all maintainers and contributors of this Guide. Read more in [CONDUCT.md](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/CONDUCT.md).

# License

The Hackathon Starter Kit is open source software [licensed as MIT](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/LICENSE.md).
