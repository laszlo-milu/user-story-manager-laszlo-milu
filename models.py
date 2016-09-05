from peewee import *
import config



# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase(config.dbname, config.name)


class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db

class UserStory(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()
