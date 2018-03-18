CREATE TABLE cites (
  id     SERIAL,
  c_char VARCHAR(30)
);

CREATE TABLE age_user (
  age_id    SERIAL PRIMARY KEY NOT NULL,
  age_group VARCHAR(20)
);

CREATE TABLE age_with_user (
  age_id  INTEGER,
  user_id INTEGER
);
CREATE TABLE tags (
  tag_id      SERIAL PRIMARY KEY NOT NULL,
  name        VARCHAR(50),
  create_date DATE               NOT NULL DEFAULT current_date,
  parent_id   INTEGER
);

CREATE TABLE tags_with_user (
  tag_id  INTEGER,
  user_id SMALLINT
);

CREATE TABLE room (
  room_id      SERIAL PRIMARY KEY NOT NULL,
  login_parent VARCHAR(20),
  create_date  DATE               NOT NULL DEFAULT current_date,
  title        VARCHAR(30),
  info_id      INTEGER,
  channel      VARCHAR(30)
);

CREATE TABLE user_in_room (
  user_id INTEGER,
  room_id INTEGER
);

CREATE TABLE users (
  user_id     SERIAL PRIMARY KEY NOT NULL,
  create_date DATE               NOT NULL DEFAULT current_date,
  name        VARCHAR(20),
  login       VARCHAR(20),
  status      VARCHAR(20),
  url_foto    VARCHAR(255),
  info        TEXT,
  search      TEXT,
  skill       TEXT,
  link        CHAR
);
