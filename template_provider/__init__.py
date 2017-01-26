from cfme.common.provider import BaseProvider


class Management(object):
    pass


@BaseProvider.add_base_type
class TemplateProvider(BaseProvider):
    provider_types = {}
    category = "template"


@TemplateProvider.add_provider_type
class MyTemplateProvider(TemplateProvider):
    type_name = "myprovider"
    mgmt_class = Management
