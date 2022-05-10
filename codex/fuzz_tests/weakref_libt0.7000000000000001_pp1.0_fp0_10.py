import weakref

# ----------------------------------------------------------------------------
class AdminView(View):
    """Administration view"""
    methods = ['GET', 'POST']
    template_name = 'admin/index.html'

    # ------------------------------------------------------------------------
    def dispatch(self, request, *args, **kwargs):
        """
        Overrides the dispatch() to store the current user in the current request.
        """
        self.request = request
        return super(AdminView, self).dispatch(request, *args, **kwargs)

    # ------------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.
        """
        context = dict()
        return render(request, self.template_name, context)

    # ------------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests.
        """
        return HttpResponseRedirect(self.get_success_url())
# ----------------------------------------------------------------------------
