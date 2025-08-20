from inven_app.models import Orgnaiztion_add


def organization_list(request):
    org = Orgnaiztion_add.objects.first()
    return {'org_name': org}