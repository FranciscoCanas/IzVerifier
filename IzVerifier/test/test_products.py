__author__ = 'fcanas'

import unittest
from IzVerifier.izspecs.containers.izconditions import IzConditions
from IzVerifier.izspecs.containers.izstrings import IzStrings
from IzVerifier.izspecs.containers.izvariables import IzVariables
from IzVerifier.izspecs.verifiers.seeker import Seeker
from IzVerifier.izverifier import IzVerifier
from IzVerifier.izspecs.izproperties import *


path1 = '' # path to install.xml
path2 = '' # path to install.xml
path3 = ''
source_paths = [] # paths to code bases
class TestProduct(unittest.TestCase):
    """
    Basic testing of seeker class.
    """

    args = {
            'specs_path': path1,
            'sources': source_paths,
            'resources_path': path2,
            'pom': path3,
            'specs': ['conditions', 'strings', 'variables']
        }

    def setUp(self):
        #self.loadInstaller(self.args)
        pass


    def loadInstaller(self, args):
        """
        Runs the verifications on some installer product.
        """

        self.verifier = IzVerifier(args)
        self.seeker = Seeker(self.verifier.paths)
        langpack = self.verifier.paths.get_langpack_path()
        self.conditions = IzConditions(self.verifier.paths.get_path('conditions'))
        self.variables = IzVariables(self.verifier.paths.get_path('variables'))
        self.strings = IzStrings(langpack)

    def verifyInstaller(self):
        """
        Run verification tests.
        """
        self.verifier.verify_all(verbosity=1)

    def test_verifyInstaller(self):
        #self.verifyInstaller()
        pass




