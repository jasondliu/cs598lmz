import types
types.ModuleType('trac.tests.functional')

from trac.web.tests.functional import *

#TODO: more tests

class TestWikiHistory(FunctionalTwillTestCaseSetup):
    def runTest(self):
        """View wiki history"""
        id = self._tester.create_wiki_page()
        self._tester.edit_wiki_page(id)
        self._tester.go_to_wiki(id)
        tc.follow('History')
        tc.url(self._tester.url + '/wiki/' + id + '\?action=history')
        tc.find('Revision History')
        tc.find('<input [^>]*checked="checked" [^>]*id="rev-1" />')
        tc.find('<input [^>]*checked="checked" [^>]*id="rev-2" />')
        tc.find('<input [^>]*id="rev-3" />')
        tc.find('<input [^>]*id="rev-4" />')
        tc.find('<
