DROP TABLE IF EXISTS no_comments;
CREATE TABLE no_comments (
  id INT PRIMARY KEY,
  name VARCHAR(10)
);

DROP TABLE IF EXISTS relations;
CREATE TABLE relations (
  id INT PRIMARY KEY,
  no_comment_id INT
);
