{
    'name': 'Multiuser TODO',
    'description': 'Estende la Todo app per farla diventare Multi Utente',
    'author': 'Metadonors',
    'depends': ['todo_app', 'mail'],
    'data': [
        'security/todo_access_rules.xml',
        'views/todo_task.xml'
    ]
}