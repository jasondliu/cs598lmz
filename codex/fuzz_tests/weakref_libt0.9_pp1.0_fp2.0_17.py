import weakref

from magmalt.parser.parser import Parser
from magmalt.model.step import StepModel, MandatoryInputError
from magmalt.context.resolver import Resolver
from magmalt.utils import Output, Status


class ContextBuilder(object):
    """
    The ContextBuilder takes a StepModel to initialize a Context,
    expected from a Step, before executing it.

    Returns a Context instance.
    """
    def build(self, step_model, resolver):
        """
        :param step_model: business model for execution (generated with parser)
        :param resolver: Dependencies resolver for context
        """
        ## Initialize Context
        status = Status.PENDING
        ouput = Output()

        ## Initialize Context
        ctx = Context(step_model)
        ctx.update_status(status)
        ctx.set_output(ouput)
        ctx.set_resolver(resolver)
        return ctx


class Context(object):
    """
    Context is the runtime support for a current step.

    The
