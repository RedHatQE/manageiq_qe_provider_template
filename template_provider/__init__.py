from cfme.common.provider import BaseProvider


class Management(object):
    pass


class TemplateProvider(BaseProvider):
    provider_types = {}
    category = "template"


class MyTemplateProvider(TemplateProvider):
    type_name = "myprovider"
    mgmt_class = Management
