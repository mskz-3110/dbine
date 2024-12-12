# dbine
Auxiliary tools related to databases

## Versions

|Version|Summary|
|:--|:--|
|0.1.0|Release dbine|

## Installation
`pip install dbine`

## Usage
![](./images/database_mysql.png)
```python
import dbine as db

type = db.Type.PostgreSQL
with db.Connection(db.ConnectionOptions(**{"Type": type, "DatabaseName": "dbine", "UserName": "reader", "Password": "READER"})) as connection:
  dbergraph = gg.Dbergraph(connection.get_database())
  dbergraph.Database.update()
  dbergraph.to_dot_helper().write_image("""./images/database_{}.pdf""".format(type.name.lower()))
```
