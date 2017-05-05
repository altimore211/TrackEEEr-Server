# TrackEEEr-Server
Code for the server, sample client, and SQLite database

#### Notes (Setting up the database):
1. Install SQLite via "sudo apt-get install sqlite"
2. Make database by "sqlite3 trackeeer"
3. Create the table after inputting "sqlite> CREATE TABLE trackeeed (tracked_user text, desc text, gen_location text, last_update text);"

## Update (May 5, 2017)
1. Filtering of data to remove Service Set Identifiers (SSIDs) and their corresponding Recieved Signal Strength Indicators (RSSIs) that are not Access Points was done in preparation for determining the general location. This filtering system was made on the assumption that the access points have a pattern to naming.
2. The maximum RSSI and the corresponding SSID is now determined by the server. This was done by adding dummy data in the code for testing.
3. Parsing of data is underway.

//The database is subject to change and was initially made for testing purposes.
