from test import *
import elasticd.resource
import os
os.environ['AWS_ACCESS_KEY_ID'] = 'ASIAIHEQDM24DWMSQBAQ'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'yoY2H58ophKHxwxp1gcThq/+BZA3rVWlVvHbPvXy'
os.environ['AWS_SECURITY_TOKEN'] = 'AQoDYXdzELL//////////wEagAPAvLeL6rRsQrO0ZZmna+JcnS1HGqU2KGvaRUVBVIYtZmY96+ou5P0uZ5r+9yi7fZjP5nV89jJROCDWlZD/wQOkmJ0roXunir4uBkXT73UQ10gbqdZVJlBq5VdLw0ehgVvLRq5rCMzp/B1uAeuOIhEuXI6fkxWHkv/FAJns3rmM7fy7g3ibk11mxpNz3Xvw+/upPCjf0R1k3OEU5W3mbQEMEWp8uTUt41ZZnStnQ/4rGjEMxnpwfc1vcKEyRKqgzOFU8YN3GG+mtWZ9m+Gz+BchFTEk4m0VRgbAgvNfoyYb3nHmrfrF2PXYkFLz2n2BNoI0CZZZDDRlRN2nH3zHXpAZneLiopOwKcFhzuY/0dSNoUzCpZLThjNakeJWZq7SMIxIUFLa1owxkaH/iBG8vuA7XnQsQ16ii8kxn1bRJ3wrx8XGE3B8BQakXNPnNwv1h+6LHwpWDvVyn9MbJtIlJj2KUOrsMuhWFjChOQMcHwfP2p5LCcnC07IzsCqwPVN0R94g/7GqrgU='

class TestAWSResourceLocator(unittest.TestCase):
    def test_init(self):
        _plugin_manager = get_test_plugin_manager('settings.arl.cfg')
        self.assertIsNotNone(_plugin_manager)

        _resource_locator = _plugin_manager.get_resource_locator()

        self._test_obj(_resource_locator, ResourceLocator)
        resources = _resource_locator.get_resources()
        # Check if list
        self.assertNotIsInstance(resources, basestring)

    def _test_obj(self, obj, cls):
        self.assertIsNotNone(obj)
        self.assertTrue(isinstance(obj, BasePlugin), '%s does not extend base plugin' % obj)
        self.assertTrue(isinstance(obj, cls), '%s does not extend %s' % (obj, cls))


if __name__ == '__main__':
    unittest.main()
