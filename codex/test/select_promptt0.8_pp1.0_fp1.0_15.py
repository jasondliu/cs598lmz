import select
# Test select.select()
select.select([sys.stdin], [], [], 0)
# Test select.poll()
select.poll()

# Test pycparser
import pycparser
import pycparser.c_generator

# Test Java classes.
import h2o
from h2o.frame import H2OFrame

# Test ML functionality
import h2o.estimators
import h2o.estimators.gbm
import h2o.estimators.random_forest
import h2o.estimators.deeplearning

# Test H2OFrame multi-column slicing
#   (requires ML functionality since H2OFrame.__getitem__() calls H2O.as_list() internally)
h2o.init(strict_version_check=False)
iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
iris[0]
iris[0:2]
iris["C1"]
