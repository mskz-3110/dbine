\encoding UTF8;

DROP TABLE IF EXISTS psql.no_comments;
CREATE TABLE psql.no_comments (
  id INT PRIMARY KEY,
  name VARCHAR(10)
);
COMMENT ON TABLE psql.no_comments IS 'コメントなしテーブル';

DROP TABLE IF EXISTS psql.with_comments;
CREATE TABLE psql.with_comments (
  id INT PRIMARY KEY,
  name VARCHAR(10)
);
COMMENT ON TABLE psql.with_comments IS 'コメントつきテーブル';
COMMENT ON COLUMN psql.with_comments.id IS 'ID';
COMMENT ON COLUMN psql.with_comments.name IS '名前';

DROP TABLE IF EXISTS psql.relations;
CREATE TABLE psql.relations (
  id INT PRIMARY KEY,
  no_comment_id INT,
  with_comment_id INT
);
COMMENT ON COLUMN psql.relations.id IS 'ID';
COMMENT ON COLUMN psql.relations.no_comment_id IS 'コメントなしテーブルのID';
COMMENT ON COLUMN psql.relations.with_comment_id IS 'コメントつきテーブルのID';
