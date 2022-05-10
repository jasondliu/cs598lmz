import weakref

from cobra.core import Object, Model, Metabolite, Reaction, Gene, Solution, DictList
from cobra.core.gene import gene_reaction_rule
from cobra.core.reaction import Reaction as ReactionCore
from cobra.core.metabolite import Metabolite as MetaboliteCore
from cobra.core.gene import Gene as GeneCore
from cobra.core.solution import Solution as SolutionCore
from cobra.core.dictlist import DictList as DictListCore
from cobra.core.model import Model as ModelCore
from cobra.core.object import Object as ObjectCore
from cobra.flux_analysis import pfba
from cobra.flux_analysis.variability import flux_variability_analysis
from cobra.io.sbml import create_cobra_model_from_sbml_file
from cobra.util.solver import set_objective
from cobra.util.util import format_long_string
from cobra.util.solver import linear_reaction_coefficients
