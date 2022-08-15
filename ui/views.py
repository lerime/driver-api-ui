from django.views.generic.base import TemplateView

from ui.services import DriverService


class DriverView(TemplateView):
    template_name = 'drivers.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data()
        driver_service = DriverService()
        params = {}
        for k, v in self.request.GET.dict().items():
            if v:
                params[k] = v

        params['limit'] = self.paginate_by
        params['offset'] = self.paginate_by * (kwargs.get('page', 1) - 1)
        kwargs['drivers'] = driver_service.get_all_records(params=params)
        return kwargs
