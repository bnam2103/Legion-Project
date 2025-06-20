def is_question_or_command(text):
    text = text.strip().lower()
    question_words = ['hello','hi','who', 'what', 'when', 'where', 'why', 'how', 'do', 'does', 'is', 'are', 'can', 'could', 'would', 'should']

    if text.endswith('?'):
        return 'question'

    for word in question_words:
        if text.startswith(word + ''):
            return 'question'

    return 'command'
