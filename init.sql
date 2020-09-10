BEGIN TRANSACTION;

CREATE TABLE 'users'('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          
           'user_id' TEXT NOT NULL,
           'user_name' TEXT);

COMMIT;
