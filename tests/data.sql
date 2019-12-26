INSERT INTO user (username, password)
VALUES
  ('cat@cat.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('dog@dog.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f');

INSERT INTO review (author_id, content)
VALUES
  (1, 'This paper is more appropriate for a speciality journal. Like, one that specializes in terrible papers.'),
  (1, 'Before I can recommend acceptance, I request the following 272 changes to the manuscript.'),
  (1, 'Let me begin by apologizing for being so late with this review – it took me much longer than expected to figure out how best to insult all the authors.');
