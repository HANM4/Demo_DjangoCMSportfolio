from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.shortcuts import render


class ProjectsListView(ListView):
    model = Project
    paginate_by = 2
    template_name = 'app_portfolio/projects.html'

    def get_queryset(self):
        return Project.objects.filter(publication=True, )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = TagName.objects.all()
        context["tag_selected_slug"] = "all"
        return context


class TagProjectsListView(ListView):
    model = TagName
    paginate_by = 2
    template_name = 'app_portfolio/projects.html'

    def get_queryset(self):
        tag_name_id = TagName.objects.filter(
            slug=self.kwargs['slug']
        ).first().pk
        return Tag.objects.filter(tag=tag_name_id, )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = TagName.objects.all()
        context["tag_selected_slug"] = self.kwargs['slug']
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "app_portfolio/project_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        """
        add toolbar for change a post
        """
        response = super().get(request, *args, **kwargs)
        request.toolbar.set_object(self.object)
        return response


def render_project_page(request, project):
    return render(request, 'app_portfolio/project_page.html',
                  { 'project': project, })