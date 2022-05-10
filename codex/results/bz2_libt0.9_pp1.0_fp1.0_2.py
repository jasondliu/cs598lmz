import bz2
bz2.BZ2File.__init__ = 5
import logging

#setup_logging()
logger = logging.getLogger(__name__)
logger.debug('HI')
    #serialize_data(pp.to_serializable_object(g), file_name)
#graph.NEXUS = os.path.join(settings.NEXUS, 'nexus')
#graph.DB = os.path.join(settings.NEXUS, 'nexus.web.db')
#'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#formatter = logging.Formatter('%(name)s:%(levelname)s: %(message)s')
#handler.setFormatter(formatter)

#logger = logging.getLogger(__name__)
#logger.addHandler(handler)
#logger.setLevel(logging.DEBUG)
#logger.debug('hi')

# @nottest
# def sample_model_update():
#     '''
#
