0x00. MySQL advanced
# Users Table Structure

The `users` table contains information about the users of the application. Below is the detailed structure of the table:

| Column  | Data Type               | Null | Key  | Default | Description                                |
|---------|-------------------------|------|------|---------|--------------------------------------------|
| `id`    | `int(11)`              | NO   | PRI  | NULL    | Unique identifier for each user (auto-incrementing primary key). |
| `email` | `varchar(255)`          | NO   | UNI  | NULL    | User's email address, must be unique.     |
| `name`  | `varchar(255)`          | YES  |      | NULL    | User's name.                               |
| `country`| `enum('US', 'CO', 'TN')` | NO  |      | 'US'    | User's country; can be 'US', 'CO', or 'TN', with 'US' as the default. |

## Example Entries

| id | email                     | name     | country |
|----|---------------------------|----------|---------|
|  1 | delisiletwala62@gmail.com | Ladydee3 | US      |
|  2 | neomolapi@gmail.com       | Neo      | US      |
|  3 | twalalethabo9@gmail.com   | Lethabo  | CO      |

## Notes
- The `country` column restricts entries to the specified enumeration values ('US', 'CO', 'TN'), defaulting to 'US' if not specified.
- The `email` column must be unique for each user to ensure proper identification and communication.


