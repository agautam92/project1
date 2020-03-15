from django.core.management.base import BaseCommand,CommandError
from user.models import CustomUser

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username',type=str,help='Choose a username')
        parser.add_argument('password',type=str,help='Choose password smartly')

    def handle(self, *args, **kwargs):
        username=kwargs['username']
        password=kwargs['password']
        CustomUser.objects.create_superuser(username,password)

