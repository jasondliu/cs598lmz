import types
# Test types.FunctionType
def makeFunctionTestDocument(isClassMethod):
    from xml.dom import minidom
    comment = """
    /**
     * @param {string} name
     * @param {Object.<string, number>} options
     * @param {number} options.fizz
     * @param {number} options.buzz
     * @constructor
     */"""
    if (isClassMethod):
        comment = comment + """

        /**
         * @param {string} name
         * @param {Object.<string, number>} options
         * @param {number} options.fizz
         * @param {number} options.buzz
         * @constructor
         */"""

    comment = comment.replace('\n', '').replace(' ', '')
    test_comment = """
    /*
     * @return {string}
     * @override
     */"""
    test_comment = test_comment.replace('\n', '').replace(' ', '')
    doc = """
    /**
     * A test namespace.
     * @namespace
     */
   
