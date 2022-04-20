# Home Price Prediction Bot


![alt text](/images/PS.png)

![alt text](/images/Task.png)

![alt text](/images/APIs.png)


# Deployment

## installation of env
```cmd
conda create -n homelane -y
conda activate homelane
pip install django djangorestframework djangorestframework-api-key
```
## django project setup
```cmd
django-admin startproject homelane
python manage.py startapp queryservice
python manage.py startapp dataservice
```
## schema creation
```cmd
python manage.py makemigrations
python manage.py migrate
```
## running server
```cmd
python manage.py runserver
```

# Data Migration
```CMD
To migrate CSV data to the SqlLite DB of django run this file
    python data_migration.py
```

# API Key Generation
```CMD
Creating & Using API Key's
    https://florimondmanca.github.io/djangorestframework-api-key/guide/#getting-started

ADMIN Credentials
    superuser username - admin
    pass - admin
    api-key = jpiUDz4N.Nmq1VTEZ2JymGDrDaouZwPW4cVFJVfPR
```
# ADMIN Console
![alt text](/images/admin.png)

# JSON Input structure
![alt text](/images/json1.png)

![alt text](/images/json2.png)

![alt text](/images/json3.png)

# API KEY Usage
![alt text](/images/Auth.png)

# DB SCHEMA 
![alt text](/images/DB.png)

# Unit Testing
![alt text](/images/Test.png)

# API Testing
![alt text](/images/api1.png)

![alt text](/images/api2.png)

![alt text](/images/api3.png)

![alt text](/images/api4.png)