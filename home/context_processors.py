
def user_info(request):
    user_role = getattr(request.user, 'role', None)

    if request.user.is_authenticated:
        return {
            'logged': True,
            'role': user_role,
            'username': request.user.username,
        }

    return { 
        'logged': False,
        'role': None,
        'username': None,
    }