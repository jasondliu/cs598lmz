import weakref
# Test weakref.ref keyword usage.
#
# Note: This test is disabled because it is 
#       relevant only in the Python implementation.
echo ">>> weakref.ref"
raise NotImplementedError("you must implement this test first")
#
# Import test/include/run_python.sh
#
echo ">>> import test/include/run_python.sh"
cp $BASE_DIR/test/include/run_python.sh $BUILD
chmod +x $BUILD/run_python.sh
# Test the import of pygccxml.declarations using Boost.Python
#
# Note: This test is disabled because it is 
#       relevant only in the Python implementation.
echo ">>> import pygccxml.declarations"
raise NotImplementedError("you must implement this test first")
# Test import of pygccxml.declarations from pygccxml.parser.

#
# Note: This test is disabled because it is 
#       relevant only in the Python implementation.
#
echo ">>> import pygccxml.declarations from pygccxml.parser"
raise Not
