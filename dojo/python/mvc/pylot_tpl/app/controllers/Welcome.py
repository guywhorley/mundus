"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from gutils.glog import *

# Controller name var used for glog messages
cn = "Welcome"

class Welcome(Controller):

    def __init__(self, action):
        glogDebug("Enter {}#__init__()...".format(cn))
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db
        glogDebug("...exit {}#__init__()".format(cn))

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        glogDebug("Enter {}#index()...".format(cn))
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """

        glogDebug("...exit {}#index()".format(cn))
        return self.load_view('index.html')

    def test(self):
        glogDebug("Enter {}#test()...".format(cn))

        glogDebug("...exit {}#test()".format(cn))
        return "<h2>Test Page</h2><p>You have reached the test page.</p>"
