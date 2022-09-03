# Boston-Data
End to End implementation of Boston Dataset

# Steps done in this Project
1. Done EDA
2. Split the data into train and test
3. Standardised the data
4. Trained the Linear Regression Model
5. Calulated the Metrics
6. Stored the model in pickle

Tools and Softwares required to deploy the project
1. GitHub Account
2. Heroku Account
3. VS CODE IDE
4. GitCLI

# Steps for deploying the project
1. Create Conda Environment
```
conda create -p python==3.7 -y
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Setup Git Enter user name details
```
git config --global user.name ""
git config --global user.email "abc@gmail.com"
```

4. Git Steps to push the code to the main branch
```
git add . - add all the files
git commit -m "message" - commits the added files with a message
git push <remote> branch - pushes to main branch
```
5. Creating an api that give predictions code using the Flask 
6. Create templates folder and home.html for render_template
7. Installed the postman to test the predict_api() function
8. Now, create a webpage so that we can pass all the input parameters in the web page and also the prediction can be seen in the web page itself

Upto now, we tested the app in offline method. Now, we can go forward and deploy the application in Heroku cloud
9. Procfile is created in the project. There are commands inside procfile so that whenever the application starts, all the commands will be run in the cloud.
 
 gunicorn - green unicorn is the python-http server for wsgi applications. It allows you to run python process concurrently.
 ex: when there are multiple users hitting the servers, gunicorn helps us to distribute the requests across instances.

 10. Done deployment in Heroku, now we are actually building the CI/CD pipeline using GitHub actions. So that, whenever we push the code GitHib it automatically deploys the entire code into production

 To create GitHub actions, we need to create github workflows folder which contains main.yaml and also add the secrets in the GitHub repository settings.

 

