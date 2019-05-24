import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    current_path = os.getcwd()

    WORK_FOLDER = current_path + '/app/uploads/'
    PATH_JSON = current_path + '/temp_config.json'

    MYMEDIALITE_FOLDER =  "/home/maxtarnavsky98/MyMediaLite"
