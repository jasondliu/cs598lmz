import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for p in Poll.objects.all():
            print p.id
            print p.name
            print p.description
            print p.pub_date
            print p.end_date
            print "-----------------"
            print "Choices:"
            for c in p.choice_set.all():
                print c.choice_text
                print c.votes
                print "-----------------"
            print "-----------------"
