activiies = [(1,3),(2,5),(3,6),(8,9),(5,7),(5,9)]

def activities_selection(activities):
    activiies.sort(key = lambda x:x[1])
    result = []
    last_end_time = 0
    for activity in activiies:
        start = activity[0]
        end = activity[1]
        if start>=last_end_time:
            result.append(activity)
            last_end_time = end
    return result

print(activities_selection(activities=activiies))        