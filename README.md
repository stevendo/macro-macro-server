[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Django Auth Template

This template contains a project, `django_auth_template`, and an app, `api`, which are set up complete with user authentication and an example resource, `Mango`, which has an example user ownership implementation.

## Preparation

1. [Download](../../archive/master.zip) this template.
1. Move the .zip file to your `sei/projects/` directory and Unzip it (creating a
   folder) -- **NOTE:** if the folder was already unzipped, use the `mv` command
   line to move it to the `sei/projects/` directory.
1. Empty [`README.md`](README.md) and fill with your own content.
1. Move into the new project and `git init`.
1. Create and checkout to a new branch, `training`, for your work.
1. Create a `.env` file
1. Add a key `ENV` with the value `development` **exactly**.
    1. Note: When you deploy, you will create this key on Heroku the value `production`. This will distinguish the development and production settings set in this template.
1. Run `pipenv shell` to start up your virtual environment.
1. Run `pipenv install` to install dependencies.
2. Create a psql database for your project
    1. Edit `settings.sql` then run `psql -U postgres -f settings.sql`
    OR:
    1. Type `psql` to get into interactive shell.
    2. Run `CREATE DATABASE "project_db_name";` where `project_db_name` is the name you want for your database.
1. Add the database name to the `.env` file using the key `DB_NAME_DEV`.
1. Replace all instances of `django_auth_template` with your application name. This includes the folder included in this repository.
2. Generate a secret key using [this tool](https://djecrety.ir) and add it to the `.env` file using the key `SECRET`.
1. Open the repository in Atom with `atom .`

### The `.env` File

After following the steps above, your `.env` file should look _something_ like
the following, replacing `project_db_name` with your database name and `secret_key`.

```sh
ENV=development
DB_NAME_DEV=project_db_name
SECRET=secret_key
```

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

## Deployment

Before deploying, make sure you have renamed your project folder and replaced all instances of `django_auth_template` with your app's name.

Once ready, you can follow the steps in the [django-heroku-deployment-guide](https://git.generalassemb.ly/ga-wdi-boston/django-heroku-deployment-guide).

## Additional Resources

- [Django Rest Framework Tutorial: Authentication](https://www.django-rest-framework.org/api-guide/authentication)

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
