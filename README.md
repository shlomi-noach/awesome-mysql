# awesome-mysql

A curated list of awesome MySQL software, libraries and tools.

This list accepts and encourages Pull Requests. See [CONTIBUTING](CONTRIBUTING.md)

### Contents

- [Awesome MySQL](#awesome-mysql)
    - [Analysis](#analysis)
    - [Backup](#backup)
    - [Connectors](#connectors)
    - [Deployment](#deployment)
    - [Development](#development)
    - [Proxy](#proxy)
    - [Replication](#replication)
    - [Schema](#schema)
    - [Server](#server)
    - [Sharding](#sharding)
    - [Toolkits](#toolkits)

- [Resources](#resources)
    - [Benchmarks](#benchmarks)
    - [Conferences](#conferences)
    - [E-Books](#e-books)
    - [Websites](#websites)
        - [Blogs](#blogs)


## Analysis

*Performance, data & structure analysis tools*

- [Anemometer](https://github.com/box/Anemometer) - Box SQL slow query monitor.
- [innodb-ruby](https://github.com/jeremycole/innodb_ruby) - A parser for InnoDB file formats, in Ruby.
- [innotop](https://github.com/innotop/innotop) - a 'top' clone for MySQL with many features and flexibility.
- [pstop](https://github.com/sjmudd/pstop) - a top-like program for MySQL, collecting, aggregating and displaying information from performance_schema.


## Backup

*Backup tools*

- [MyDumper](https://launchpad.net/mydumper) - Logical, parallel backup/dumper tool for MySQL
- [Percona Xtrabackup](http://www.percona.com/doc/percona-xtrabackup) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.


## Connectors

*MySQL connectors for various programming languages*

- [Connector/Python](https://dev.mysql.com/downloads/connector/python/) - a standardized database driver for Python platforms and development.
- [go-sql-driver](https://github.com/go-sql-driver/mysql) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
- [MySQL-Python](http://sourceforge.net/projects/mysql-python/) - MySQL database connector for Python programming.


## Deployment

*MySQL deployment tools*

- [MySQL Sandbox](http://mysqlsandbox.net/) - a tool that installs one or more MySQL servers within seconds, easily, securely, and with full control.


## Development

*Tools to support MySQL-related development*

- [Flywaydb](http://flywaydb.org/getstarted/) - Database migrations; Evolve your database schema easily and reliably across all your instances
- [Liquibase](http://www.liquibase.org/) - Source control for your database
- [Propagator](https://github.com/outbrain/propagator) - Centralized schema & data deployment on a multi-everything topology


## Proxy

*Proxies to MySQL*

- [MaxScale](https://github.com/mariadb-corporation/MaxScale) - open-source, database-centric proxy.
- [MySQL Proxy](https://launchpad.net/mysql-proxy) - A simple program that sits between your client and MySQL server(s) that can monitor, analyze or transform their communication.
- [ProxySQL](https://github.com/renecannao/proxysql) - High performance proxy for MySQL.


## Replication

*Replication related software*

- [orchestrator](https://github.com/outbrain/orchestrator) - MySQL replication topology management and visualization tool.
- [Tungsten Replicator](http://code.google.com/p/tungsten-replicator/) - A high performance, open source, data replication engine for MySQL.


## Schema

*Add-on schemas*

- [common_schema](http://code.google.com/p/common-schema/) - DBA's framework for MySQL, providing a function library, views library and QueryScript interpreter.
- [sys](https://github.com/MarkLeith/mysql-sys) - A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage.


## Server

*MySQL server flavors*

- [MariaDB](https://github.com/MariaDB/server) - Community developed fork of MySQL server.
- [MySQL Server & MySQL Cluster](https://github.com/mysql/mysql-server) - Official Oracle's MySQL server & MySQL Cluster distribution.
- [Percona Server](https://launchpad.net/percona-server) - An enhanced, drop-in MySQL replacement.
- [WebScaleSQL](https://github.com/webscalesql/webscalesql-5.6) - WebScaleSQL, Version 5.6, based upon the MySQL-5.6 community releases.


## Sharding

*Sharding solutions/frameworks*

- [vitess](https://github.com/youtube/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.


## Toolkits

*Toolkits, general purpose scripts*

- [Percona Toolkit](http://www.percona.com/software/percona-toolkit) - a collection of advanced command-line tools to perform a variety of MySQL server and system tasks that are too difficult or complex to perform manually.
