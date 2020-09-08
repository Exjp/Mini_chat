CREATE SCHEMA mini_chat;
SET search_path TO mini_chat, public;

);
CREATE TABLE mini_chat.Username (
  pseudo text NOT NULL,
  mdp text NOT NULL,
  PRIMARY KEY(pseudo)
);

CREATE TABLE mini_chat.chat (
  pseudo text NOT NULL,
  messages text NOT NULL,
  id serial PRIMARY KEY
);
