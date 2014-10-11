from django.test import LiveServerTestCase
from google.appengine.ext import testbed

class GAELiveServerTestCase(LiveServerTestCase):
    '''Extends LiveServerTestCase with GAE stubs so that the tests can run
    under the GAE environment. This is useful for Selenium integration tests.

    Consider adding additional testbed stubs as needed.
    '''

    @classmethod
    def setUpClass(cls):
        cls.testbed = testbed.Testbed()
        cls.testbed.activate()
        cls.testbed.init_datastore_v3_stub()
        cls.testbed.init_memcache_stub()

        super(GAELiveServerTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.testbed.deactivate()
        super(GAELiveServerTestCase, cls).tearDownClass()
