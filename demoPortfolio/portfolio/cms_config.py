from cms.app_base import CMSAppConfig

from .models import Project
from .views import *


class PortfolioAppConfig(CMSAppConfig):
    cms_enabled = True
    #cms_toolbar_enabled_models = [(Project, ProjectDetailView.as_view())]
    cms_toolbar_enabled_models = [(Project, render_project_page)]
