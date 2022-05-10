import weakref


class ContentManager(object):
    def __init__(self, manager, jobTypeID=None, contentTypes=None):
        self.manager = weakref.proxy(manager)

        if jobTypeID is None:
            raise ValueError("jobTypeID is None")

        self.jobTypeID = jobTypeID
        self.contentTypes = contentTypes

        self.manager.app.logger.info("JobTypeID: %s", jobTypeID)
        self.manager.app.logger.info("ContentTypes: %s", contentTypes)

    def getJobTypeID(self):
        return self.jobTypeID

    def addContentType(self, contentType):
        self.contentTypes.append(contentType)

    def getContentTypes(self):
        return self.contentTypes

    def getContentTypeByID(self, contentTypeID):
        for ct in self.contentTypes:
            if ct.getID() == contentTypeID:
                return ct
        return None

