import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def drop_duplicates_events():
	events_data = get_events_from_app_events()
	events_data.drop_duplicates(subset=['event_id'], keep='first', inplace=True)
	print(events_data.columns.values)
	print(events_data.shape)
	return events_data


def drop_duplicates_usre_actions(events_data):
	user_actions_data = get_user_actions_from_app_events()
	user_actions_data.drop_duplicates(subset=['user_id', 'event_id', 'is_installed', 'is_active', 'action'],
	                                  keep='first', inplace=True)
	merge = pd.merge(events_data, user_actions_data, how='inner', on=['event_id', 'user_id'])
	print(merge.columns.values)
