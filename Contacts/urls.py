from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^$', views.contacts_list, name='contacts_list'),
url(r'^contacts/(?P<id>\d+)/$', views.contact_details, name='contact_details'),
url(r'^contacts/new/$', views.new_contact, name='new_contact'),
url(r'^contacts/(?P<id>\d+)/edit$', views.edit_contact, name='edit_contact'),

]