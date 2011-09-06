import datetime

from django.db.models import Sum
from django.db.models.query import QuerySet

from user_activity.models import Activity, ActivityType 



class InvalidActivityType(Exception):
    pass


def register_activity(user, activity_type, hits=1, timestamp=None):
    #register user activity at DB
    if isinstance(activity_type, basestring): 
        try:
            activity_type_obj = ActivityType.objects.get(keyname=activity_type)
        except ActivityType.DoesNotExist, ex:
            raise InvalidActivityType(activity_type)
    elif isinstance(activity_type, ActivityType):
        activity_type_obj = activity_type
        
    values = {
        'user' : user, 
        'activity_type' : activity_type_obj, 
        'hits' : hits
    }
    if timestamp:
        values.update(timestamp=timestamp)
    
    user_activity_obj = Activity.objects.create(**values)
    

    
    
def get_resume_activities_by_user(user, from_date=None, to_date=None):
    if isinstance(from_date, datetime.datetime):
        from_date = from_date.date()
    if isinstance(to_date, datetime.datetime):
        to_date = to_date.date()
    filters = {'user' : user}
    if from_date:
        filters['timestamp__gte'] = from_date
    if to_date:
        filters['timestamp__lt'] = to_date + datetime.timedelta(days=1)
    
    return Activity.objects \
                   .filter(**filters) \
                   .values('activity_type__id', 'activity_type__keyname', 'activity_type__label',) \
                   .annotate(count=Sum('hits'))
                   
def get_resume_activities_by_users(users, from_date=None, to_date=None):
    if isinstance(from_date, datetime.datetime):
        from_date = from_date.date()
    if isinstance(to_date, datetime.datetime):
        to_date = to_date.date()
    filters = {'user__in' : users}
    if from_date:
        filters['timestamp__gte'] = from_date
    if to_date:
        filters['timestamp__lt'] = to_date + datetime.timedelta(days=1)
    
    return Activity.objects \
                   .filter(**filters) \
                   .values('user__id', 'user__first_name', 'user__last_name', 'activity_type__id', 'activity_type__keyname', 'activity_type__label',) \
                   .annotate(count=Sum('hits'))
