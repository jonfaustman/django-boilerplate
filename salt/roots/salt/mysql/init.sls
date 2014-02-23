mysql-server:
    pkg.installed

mysql-client:
    pkg.installed

python-mysqldb:
    pkg.installed


mysql:
    service:
        - running
    require:
        - pkg: mysql-server
        - pkg: python-mysqldb
        - pkg: mysql-client

mysql-dstegelman:

    mysql_database.present:
        - name: dstegelman
        - require:
            - service: mysql

    mysql_user.present:
        - name: dstegelman
        - password: "1234"
        - require:
            - service: mysql

    mysql_grants.present:
        - grant: all privileges
        - database: dstegelman.*
        - user: dstegelman
        - require:
            - service: mysql
