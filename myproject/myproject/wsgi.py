import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

# Ensure the application binds to the correct host and port
if os.environ.get('PORT'):
    application.run(host='0.0.0.0', port=int(os.environ['PORT']))


