##############################################################################
# Documentation
##############################################################################

##############################################################################
# Imports
##############################################################################

from python_qt_binding.QtCore import QObject

##############################################################################
# Classes
##############################################################################

class RosBehaviourTreeCreator(QObject):
    no_roscore_switch = "--no-roscore"

    def __init__(self, context):
        super(RosBehaviourTreeCreator, self).__init__(context)

    @staticmethod
    def add_arguments(parser, group=True):
        pass