from Products.CMFCore.utils import getToolByName
from opencore.interfaces import IProject
from opencore.svenweb.interfaces import ISvenwebFeatureletInstalled
from opencore.utility.interfaces import IHTTPClient
from opencore.utility.interfaces import IProvideSiteConfig
from plone.memoize.instance import memoizedproperty, memoize
from topp.featurelets.base import BaseFeaturelet
from topp.featurelets.interfaces import IFeaturelet
from zope.component import getUtility
from zope.interface import implements
import logging

log = logging.getLogger('opencore.svenweb')


class SvenwebFeaturelet(BaseFeaturelet):
    # could we make featurlets named utilities?
    # currently featurelet all have the same state always
    """
    A featurelet that installs a Svenweb
    """

    implements(IFeaturelet)

    id = "wikis"
    title = "Extra Wikis"
    installed_marker = ISvenwebFeatureletInstalled

    _required_interfaces = BaseFeaturelet._required_interfaces + (IProject,)
    _info = {'menu_items': ({'title': u'Wikis',
                             'description': u'Extra wikis',
                             'action': 'wikis'
                             },
                            ),
             }

