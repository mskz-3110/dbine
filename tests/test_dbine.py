import dbine as db
import graspgraph as gg

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
  for type in [db.Type.PostgreSQL, db.Type.MySQL]:
    connectionConfig = db.ConnectionConfig(**{"Type": type, "DatabaseName": "db", "UserName": "_user_", "Password": "pass"})
    yamlFilePath = """./images/connection_options_{}.yaml""".format(type.name.lower())
    connectionConfig.save(yamlFilePath)
    connectionConfig.load(yamlFilePath)
    with db.Connection(connectionConfig) as connection:
      prefix = """./images/database_{}""".format(type.name.lower())
      pdfFilePath = gg.Path.join(prefix, "pdf")
      pngFilePath = gg.Path.join(prefix, "png")
      dbergraph = gg.Dbergraph(connection.get_database())
      dbergraph.Database.update().save(gg.Path.join(prefix, "yaml"))
      dbergraph.to_dot_helper().write_image(pdfFilePath)
      gg.Pdf.convert(pdfFilePath, pngFilePath)
