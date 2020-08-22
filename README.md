# django-upload-example
Simple Django example of file upload

Features
--------
1. Basic User authorisation and registration.
2. Basic upload form.



Planned Modules
----------
Multi file upload form


Main requirements
------------

1. `python` 3.5, 3.6, 3.7
2. `Django` 3.1
3. `PostreSQL` 11.1

This project also uses a few external packages (see `requirements.txt` file for details).


## How to set up

### Setup using Docker

The easiest way to get this project up and running is via [Docker](https://www.docker.com/). See [docs](https://docs.docker.com/get-started/) to get started. Once set up run the following command:

`docker-compose up`

It may take a while for the process to complete, as Docker needs to pull required dependencies. Once it is done, the application should be accessible at `0.0.0.0:8000`. 

### Manual setup

Firstly, create a new directory and change to it:

`mkdir django-upload-example && cd django-upload-example`

Then, clone this repository to the current directory:

`git clone https://github.com/agiledesign2/django-upload-example.git .`


Next, one needs to setup database like SQLite or PostgreSQL on a local machine. This project uses PostgreSQL by default (see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#databases) for different setup). This process may vary from one OS to another, eg. on Arch Linux one can follow a straightforward guide [here](https://wiki.archlinux.org/index.php/PostgreSQL).

The database settings are specified in `website/settings/dev.py`. In particular the default database name is `BlogDjango`, which can be created from the PostgreSQL shell by running `createdb BlogDjango`.


Next, set up a virtual environment and activate it:

`python3 -m venv env && source env/bin/activate`

Install required packages:

`pip3 install -r requirements.txt`

Next, perform migration:

`python3 manage.py migrate --settings=website.settings.dev`

The setup is complete. Run a local server with

`python3 manage.py runserver --settings=website.settings.dev`

The blog should be available at `localhost:8000`.

## What's next?

At this point you can help and update the proyect with your github account.

