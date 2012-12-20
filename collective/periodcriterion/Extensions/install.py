from collective.periodcriterion import logger

def uninstall(portal, reinstall=False):
    setup_tool = portal.portal_setup
    setup_tool.runAllImportStepsFromProfile('profile-collective.periodcriterion:uninstall')
    logger.info("collective.periodcriterion has been removed")