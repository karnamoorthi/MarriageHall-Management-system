from django.urls import path
from wedapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

#Coustom view pages
	path('',views.home),
	path('login',views.login),
	path('log',views.log),
	path('register',views.register),
	path('reg',views.reg),
	path('forgot',views.forgot),
	path('call',views.call),
	path('chat',views.chat),
	path('reserve/<int:id>',views.reserve),
	path('edit/<int:id>',views.edit),
	path('order',views.order),
	path('editorder',views.editorder),
	path('face',views.face),
	path('blank',views.blank),
	path('logout',views.logout),
	path('viewdate',views.viewdate),


#Hall user
	path('detail',views.detail),
	path('alter',views.alter),
	path('ed/<int:id>',views.ed),
	path('date',views.date),

	
#admin view pages	
	path('got',views.got),
	path('front',views.front),
	path('view',views.view),
	path('Add',views.Add),
	path('Addedit',views.Addedit),
	path('deletehall/<int:id>',views.deletehall),
	path('hall',views.hall),
	path('tablelogin',views.tablelogin),
	path('tablebook',views.tablebook),
	path('delete/<int:id>',views.delete),
	path('deletelogin/<int:id>',views.deletelogin),
	path('dash',views.dash),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)