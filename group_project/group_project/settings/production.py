from group_project.settings.common import *

from environs import Env

env = Env()
env.read_env()

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
