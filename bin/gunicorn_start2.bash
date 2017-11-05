#!/bin/bash

NAME="ideations"                              #Name of the application (*)
DJANGODIR=/home/ubuntu/ideations/             # Django project directory (*)
SOCKFILE=/home/ubuntu/ideations/run/gunicorn.sock       # we will communicate using this unix socket (*)
USER=root                                        # the user to run as (*)
GROUP=www-data                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=ideations.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=ideations.wsgi                     # WSGI module name (*)
#MAX_REQUESTS={{ gunicorn_max_requests }}
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/ubuntu/ideations/myv2/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ubuntu/ideations/myv2/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
 # --max-requests $MAX_REQUESTS \
  --log-level=debug \
  --log-file=-
