import dbine as db
import graspgraph as gg
from pyemon.path import *

def test_dbine():
  assert(db.Type.PostgreSQL.name == "PostgreSQL")
  assert(db.Type.from_name(db.Type.PostgreSQL) == db.Type.PostgreSQL)
  assert(db.Type.from_name("PostgreSQL") == db.Type.PostgreSQL)
  assert(db.Type.from_value(db.Type.PostgreSQL) == db.Type.PostgreSQL)
  assert(db.Type.from_value(db.Type.PostgreSQL.value) == db.Type.PostgreSQL)
  assert(db.Type.MySQL.name == "MySQL")
  assert(db.Type.from_name(db.Type.MySQL) == db.Type.MySQL)
  assert(db.Type.from_name("MySQL") == db.Type.MySQL)
  assert(db.Type.from_value(db.Type.MySQL) == db.Type.MySQL)
  assert(db.Type.from_value(db.Type.MySQL.value) == db.Type.MySQL)

  connectionConfig = db.ConnectionConfig(**{"Type": db.Type.PostgreSQL, "DatabaseName": "db", "UserName": "_user_", "Password": "pass"})
  assert(connectionConfig.to_string() == "dbname=db host=localhost port=0 user=_user_ password=pass")
  connectionConfig = db.ConnectionConfig(**{"Type": db.Type.MySQL, "DatabaseName": "db", "UserName": "_user_", "Password": "pass"})
  assert(connectionConfig.to_string() == "{'database': 'db', 'host': 'localhost', 'port': 0, 'user': '_user_', 'password': 'pass'}")

  for type in [db.Type.PostgreSQL, db.Type.MySQL]:
    connectionConfig = db.ConnectionConfig(**{"Type": type, "DatabaseName": "db", "UserName": "_user_", "Password": "pass"})
    yamlFilePath = """./images/connection_config_{}.yaml""".format(type.name.lower())
    connectionConfig.save(yamlFilePath)
    connectionConfig.load(yamlFilePath)
    with db.Connection(connectionConfig) as connection:
      prefix = """./images/database_{}""".format(type.name.lower())
      pdfFilePath = Path.join(prefix, "pdf")
      pngFilePath = Path.join(prefix, "png")
      dbergraph = gg.Dbergraph(connection.get_database())
      dbergraph.Database.update().save(Path.join(prefix, "yaml"))
      dbergraph.to_dot().Write(pdfFilePath)
      gg.Pdf.convert(pdfFilePath, pngFilePath)
