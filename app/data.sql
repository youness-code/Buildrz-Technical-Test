CREATE TABLE IF NOT EXISTS parcelle (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  adresse VARCHAR(200) NOT NULL,
  code_postal INTEGER NOT NULL,
  ville VARCHAR(100) NOT NULL,
  surface DOUBLE NOT NULL
);

CREATE TABLE IF NOT EXISTS projet (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  parcelle INTEGER NOT NULL,
  ca DOUBLE NOT NULL
  cree_le TIMESTAMP NOT NULL,
  status VARCHAR(50) NOT NULL,
  FOREIGN KEY (parcelle) REFERENCES parcelle (id)
);


INSERT INTO parcelle(id, adresse , code_postal, ville, surface) values
(9310000100234, '30 rue de paris', 93100, 'Montreuil', 180)

INSERT INTO projet(id, parcelle , ca, cree_le, statut) values
(321, 9310000100234, 2000000, '2021-05-03', 'en cours')