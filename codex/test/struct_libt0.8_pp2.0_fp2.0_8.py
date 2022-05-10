import _struct

from cobra.model.infra import AttEntityP
from cobra.internal.codec.xmlcodec import toXMLStr

from cobra.mit.meta import PropMeta
from cobra.mit.meta import Category
from cobra.mit.meta import SourceRelationMeta
from cobra.mit.meta import NamedSourceRelationMeta
from cobra.mit.meta import TargetRelationMeta
from cobra.mit.meta import DeploymentPathMeta, DeploymentCategory
from cobra.model.category import MoCategory, PropCategory, CounterCategory
from cobra.mit.mo import Mo


# ##################################################
class InfraAttEntityP(Mo):
    """
    The infrastructure association to an entity profile.

    """

    meta = ClassMeta("cobra.model.infra.InfraAttEntityP")

    meta.moClassName = "infraInfraAttEntityP"
    meta.rnFormat = "entityp-%(id)s"
    meta.category = MoCategory.REGULAR
    meta.label = "Infra Deployment to Attachable Entity Profile"
