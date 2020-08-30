
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# which ad platform is getting the most views.
views_by_utm_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()

# Does users click on the ad?
ad_clicks['is_click']= ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

click_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = click_by_source.pivot(
  columns='is_click',
  index = 'utm_source',
  values ='user_id'
).reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] +clicks_pivot[False])

print(clicks_pivot)

# Analyzing A/B Test
num_A_B = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(num_A_B)

user_clicks_in_AB = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

print(user_clicks_in_AB)

clicks_pivot_AB = user_clicks_in_AB.pivot(
  columns ='is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()

print(clicks_pivot_AB)

# seperate A clicks and B clicks
a_clicks = ad_clicks[ad_clicks.experimental_group =='A']

b_clicks = ad_clicks[ad_clicks.experimental_group =='B']

a_clicks_by_day = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
a_clicks_by_day_pivot = a_clicks_by_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

a_clicks_by_day = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_clicks_by_day_pivot = a_clicks_by_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

a_clicks_by_day_pivot['percent_of_click']=a_clicks_by_day_pivot[True]/(a_clicks_by_day_pivot[True]+ a_clicks_by_day_pivot[False])
print(a_clicks_by_day_pivot)

b_clicks_by_day_pivot['percent_of_click']=b_clicks_by_day_pivot[True]/(b_clicks_by_day_pivot[True]+ b_clicks_by_day_pivot[False])

print(b_clicks_by_day_pivot)

#overalll Ad A has higher percent of click, I 
#recommend company use Ad A
