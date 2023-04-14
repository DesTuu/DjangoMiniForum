def category_sort_key(topic):
    if topic.name.lower() == 'inne':
        return 'zzz'
    return topic.name.lower()