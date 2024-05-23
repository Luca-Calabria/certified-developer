# supportbot test business logic

def test_supportbot(text_msg:str):
    """_summary_

    Parameters
    ----------
    text_msg : str
        test parameter for bot response
    
    Returns
    -------
    str
        hardcoded response if text_msg string is 'help'
    """
    bot_status = 'bring the harvester in for maintenance' if text_msg == 'help' else 'No Maintenance needed'
    
    return bot_status