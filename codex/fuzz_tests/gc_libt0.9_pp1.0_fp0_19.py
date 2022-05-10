import gc, weakref

# to be used for populating the 'body_of_transmission' dropdown
BODY_OF_TRANSMISSION_OPTIONS = ['', 'Email', 'Physical']

class OrganisationResource(dbresource.DBAutoSchemaResource):
    """Restful interface for accessing Organisations
        - behaves just like dbresource.DBAutoSchemaResource except it utilises
          the 'model' property to only expose required columns.
        - does not allow 'modify' of request as this is handled through ckan."""

    # every organisation has metadata associated, which we don't want to expose
    metadata = {'exclude': True}

    class Meta:
        # grab resource_name and schema from SuperClass
        resource_name = dbresource.DBAutoSchemaResource.Meta.resource_name
        schema = dbresource.DBAutoSchemaResource.Meta.schema

        # use resource methods
        allowed_methods = ["get"]

        # only expose 'public' data on our model
        model = Organisation
        allow_sub_resources = True

        # Enforce authentication for all
