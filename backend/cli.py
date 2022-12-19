# encoding: utf-8
"""
Webserver CLI
-------------
Open a terminal in the root directory of this project.
Make sure to activate your virtualenvironment and set FLASK_APP to `webserver.py` in your environment variables.

Windows:
```
set FLASK_APP=webserver.py
```

Unix
```
export FLASK_APP=webserver.py
```

With the command `flask` you can discover all the available webserver commands.

--=- generated by flask-install: https://github.com/0x78f1935/flask-install -=--
"""


def register(app) -> None:
    @app.cli.group()
    def system():
        """System sub command"""
        pass

    @system.command()
    def init():
        """Populate database with data required for CMS"""
        from backend.models import SystemTaskModel
        from backend.extensions import db
        print("* Populating database...")
        tasks = [
            {
                'sysname': 'downloader',
                'name': 'Download Assets',
                'description': 'Obtain / download available assets. Assets which already have been acquired by the host will be skipped.',
            },
            {
                'sysname': 'converter',
                'name': 'Convert Assets',
                'description': 'Try to convert assets downloaded from the previous step. Assets which failed couldn\'t be downloaded from available assets. Better luck next time.',
            },
            {
                'sysname': 'emulator',
                'name': 'Check Emulator',
                'description': 'Ping the emulator for a valid connection',
            },
        ]
        for task in tasks:
            if not SystemTaskModel.query.filter(SystemTaskModel.sysname==task['sysname']).first():
                system_task = SystemTaskModel(**task)
                db.session.add(system_task)
        db.session.commit()

        print("* Populating database Finished!")
