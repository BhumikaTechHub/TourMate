 ''' user_id = request.args.get('user_id',0)
    if user_id is None:
    # Handle the case where 'user_id' is missing
        return "user_id is required", 400  # Return a bad request response
    user_id = int(user_id) '''