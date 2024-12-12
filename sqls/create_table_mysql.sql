DROP TABLE IF EXISTS no_comments;
CREATE TABLE no_comments (
  id INT PRIMARY KEY,
  name VARCHAR(10)
) COMMENT 'コメントなしテーブル';

DROP TABLE IF EXISTS with_comments;
CREATE TABLE with_comments (
  id INT PRIMARY KEY COMMENT 'ID',
  name VARCHAR(10) COMMENT '名前'
) COMMENT 'コメントつきテーブル';

DROP TABLE IF EXISTS relations;
CREATE TABLE relations (
  id INT PRIMARY KEY COMMENT 'ID',
  no_comment_id INT COMMENT 'コメントなしテーブルのID',
  with_comment_id INT COMMENT 'コメントつきテーブルのID'
);
