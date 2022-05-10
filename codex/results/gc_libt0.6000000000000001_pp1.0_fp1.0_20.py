import gc, weakref

# =============================================================================
class S3WorkflowModel(S3Model):
    """
        Workflow Extension for Resources
    """

    names = ["s3_workflow",
             "s3_workflow_config",
             "s3_workflow_role",
             "s3_workflow_permission",
             "s3_workflow_ui_status",
             ]

    def model(self):

        T = current.T
        db = current.db

        crud_strings = current.response.s3.crud_strings

        add_component = self.add_component
        configure = self.configure
        define_table = self.define_table
        super_link = self.super_link

        # ---------------------------------------------------------------------
        # Workflow
        #
        tablename = "s3_workflow"
        table = define_table(tablename,
                             self.super_link("doc_id", "doc_entity"),
                             self.super_link("pe_id", "pr_pentity"),
                             Field("status",
                
