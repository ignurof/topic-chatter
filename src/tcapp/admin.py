from django.contrib import admin

# from .models import *
models = ["topic", "comment"]
model_list = []

# https://stackoverflow.com/questions/24940545/how-to-import-modules-given-a-list-of-their-names
for model in models:
    pass
    # globals()[model] = __import__(model)
    # admin.site.register(globals()[model])
