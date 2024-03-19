# ORAD Project modified !!

## **Don't Merge to Main or master !!!**

### Getting Started

```
$ pipenv shell

```

### Prerequisites

\*get pipenv

```
Debian- sudo apt install pipenv
```

```
Windows- pip install --user pipenv
```

```
Locate python interpreter
$ pipenv --py
/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre/bin/python

```

\*get all requirements in the Pipfile.lock

```
$ pipenv install
```

### Installing

Ensure that the MODE in the .env is set to development ('dev'), which will automatically set debug to true.

Now run the following command

```
python3.9 manage.py runserver

```

And view the site at the port provided which is most likely 127.0.0.1:8000

### Changelog

1. I have removed duplicate folders
2. Renamed folders
3. Renamed the project -> calling the project test_database is not good practice. I called the project Dashboard
4. Removed the Documents in the root -> it is now available in the media folder
5. Removed requirements.txt since the project is using pipenv so no need of requirements.txt
6. Remove frontend folder also since it was not being used

### Should Fix

1. Dockerfile should use pipenv and then to pip look here for more details [link1](https://marioyepes.com/blog/django-docker-deploy-env/) [lik2](https://gist.github.com/cse031sust02/f149d809d50116e7890691d73922d379)
2. Docker compose should at least use postgres and link it to the app not using sqlite
3.

## Conclusion

Great job guys'
