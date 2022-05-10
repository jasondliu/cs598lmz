import weakref


_logger = logging.getLogger(__name__)


class BrowserView(View):
    def __init__(self, cr, uid, model, context=None, domain=None,
                 views_preload=None, **kwargs):
        self.context = (context or {}).copy()
        self.domain = domain or []
        self.model = model
        self.views_preload = views_preload
        self.cr = cr
        self.uid = uid

        self.result_count = None
        self.res_ids = None

        self.datamanager = browse_record_list(self.cr, uid, model, context=self.context, domain=self.domain)

        for name in kwargs.pop('toolbar', []):
            getattr(self.datamanager, name)(self.context, domain)

        self.view_id = kwargs.pop('view_id', None)
        self.default_view = kwargs.pop('view_type', 'form')

        self.set_group_
