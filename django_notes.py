# {Django Intial Commands and Files}
# init.py file: Tells Python that this directory should be considered a python directory
# Settings.py: Tells about the settings of the project 
# urls.py: Contains the Urls for your project. Just like Table of Contents Files
# python manage.py runserver: To run the Django Server
# python manage.py startapp : To make an App. Add an App name after startup. Be sure that it is in the Folder where your Manage.py is

# {View Commands and Files}
# View: A View in Django is a Callable which takes a request and returns as response. To Call a View you need to add the view as a callable in the URLS config. ie the urls.py file.
# Include function from django.urls helps to refer to other URLconfs


# Arguments in a path() function:
# 1. Route: The Url Route on which the response will be rendered. 
# 2. Views: The View Function it is a part of. Eg views.index.
# 3. name: The Name you want to give it