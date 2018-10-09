# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import affinitic.ploneintranet


class AffiniticPloneintranetLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=affinitic.ploneintranet)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'affinitic.ploneintranet:default')


AFFINITIC_PLONEINTRANET_FIXTURE = AffiniticPloneintranetLayer()


AFFINITIC_PLONEINTRANET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(AFFINITIC_PLONEINTRANET_FIXTURE,),
    name='AffiniticPloneintranetLayer:IntegrationTesting',
)


AFFINITIC_PLONEINTRANET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AFFINITIC_PLONEINTRANET_FIXTURE,),
    name='AffiniticPloneintranetLayer:FunctionalTesting',
)


AFFINITIC_PLONEINTRANET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        AFFINITIC_PLONEINTRANET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AffiniticPloneintranetLayer:AcceptanceTesting',
)
